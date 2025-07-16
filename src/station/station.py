import board
import busio
import digitalio
import adafruit_rfm69
import time
import json

class Station:
    def __init__(self):
        self.rfm = self.create_rfm69(board.GP6, board.GP7, board.GP4, board.GP5, board.GP13)
        self.last_rssi = 0
    
    @staticmethod
    def create_rfm69(SCK, MOSI, MISO, CS, RESET) -> adafruit_rfm69.RFM69:
        # create the spi bus
        spi = busio.SPI(SCK, MOSI, MISO)
        # chip select and reset pins
        cs = digitalio.DigitalInOut(CS)
        reset = digitalio.DigitalInOut(RESET)
        # Initialize the radio
        rfm = adafruit_rfm69.RFM69(spi, cs, reset, 434.0, baudrate=2000000)
        encryption_key = "VB6CYeaOtduNZcgu"
        rfm.encryption_key = encryption_key
        rfm.tx_power = 13
        return rfm
    
    @staticmethod
    def process_data(raw_packet):
        try:
            packet_text = str(raw_packet, "ascii")
            #print(f"Recieved (ASCII): {packet_text}")
        
            return packet_text
        except UnicodeError:
            print(f"ERROR decoding (ASCII) data! HEX: {[hex(x) for x in raw_packet]}")
            return "STATUS_ERROR"
    
    @staticmethod
    def process_packet(packet_text, status, data_type) -> str:
        """
        Radio Handshake: ...
        """
        # discard if text is invalid
        if packet_text == "STATUS_ERROR":
            return status
        
        if packet_text == "REQUEST_DATA":
            return "DATA_TYPE"
        
        if packet_text == "RECIEVE_DATA_TYPE":
            return data_type
        
        if packet_text == "SET_DATA_TYPE":
            return "SEND_DATA"
        
        if packet_text == "SUCCESS":
            return "EXIT_SUCCESS"
        
        # assume it's legit data
        return "STATUS"
        
    # data type is type of sensor data (e.g. pressure, altitude, etc)
    def request_data(self, data_type):
        status = "REQUEST_DATA"
        data = ""
        running = True
        while running:
            self.rfm.send(bytes(status, "utf-8"))
            packet = self.rfm.receive()
            if packet is None:
                print("Recieved nothing! Listening again...")
            else:
                packet_text = self.process_data(packet)
                rssi = self.rfm.last_rssi
                self.last_rssi = rssi
                
                status = self.process_packet(packet_text, status, data_type)
                if status == "STATUS":
                    data = packet_text
                    #print(f"RECIEVED SENSOR DATA: {data}")
                if status == "EXIT_SUCCESS":
                    return data
    
    @staticmethod
    def parse_data(json_data) -> dict | str:
        try:
            data = json.loads(json_data)
            return data
        except ValueError:
            print(f"ERROR: Failed to load json from `{json_data}`! Please check if the data is json.")
            return "smoking hot garbage"


station = Station()
while True:
    data = station.parse_data(station.request_data("bmp"))
    try:
        print(data["bmp"]["temp"])
    except TypeError:
        print(f"ERROR: Failed to read from `{data}`")