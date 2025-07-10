import board
import busio
import digitalio
import adafruit_rfm69
import time
import json

class Station:
    def __init__(self):
        self.rfm = self.create_rfm69(board.GP6, board.GP7, board.GP4, board.GP5, board.GP13)
    
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
            print(f"Recieved (ASCII): {packet_text}")
        
            return packet_text
        except UnicodeError:
            print(f"ERROR decoding (ASCII) data! HEX: {[hex(x) for x in raw_packet]}")
            return "STATUS_ERROR"
    
    @staticmethod
    def process_packet(packet_text, status, data_type) -> str:
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
                print(f"Recieved signal strength: {rssi} dB")
                
                status = self.process_packet(packet_text, status, data_type)
                if status == "STATUS":
                    data = packet_text
                    print(f"RECIEVED SENSOR DATA: {data}")
                if status == "EXIT_SUCCESS":
                    return data


station = Station()
while True:
    data = station.request_data("pressure")
    print(f"Parsing data: {data}")
"""
# Create the SPI bus
spi = busio.SPI(board.GP6, board.GP7, board.GP4)  # SCK, MOSI, MISO

# Chip select and reset pins
cs = digitalio.DigitalInOut(board.GP5)
reset = digitalio.DigitalInOut(board.GP13)



print("CanSat Ground Station Init")

while True:
    
    #time.sleep(1)
    #print("Waiting for packets...")
    #rfm.send(bytes("qwertyuioplkjhgfdsazxcv" * 2,"utf-8"))
    packet = rfm.receive()
    # Optionally change the receive timeout from its default of 0.5 seconds:
    # packet = rfm9x.receive(timeout=5.0)
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        #pass
        # Packet has not been received
        print("Received nothing! Listening again...")
    else:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print(f"Received (raw bytes): {packet}")
        # And decode to ASCII text and print it too.  Note that you always
        # receive raw bytes and need to convert to a text format like ASCII
        # if you intend to do string processing on your data.  Make sure the
        # sending side is sending ASCII data before you try to decode!
        try:
            packet_text = str(packet, "ascii")
            #print(time.time())
            
            print(f"Received (ASCII): {packet_text}")
            try:
                data = json.loads(packet_text)
                print(f"data: {data}")
            except ValueError:
                print(f"Error: {packet_text}, is content JSON?")
        except UnicodeError:
            print("Hex data: ", [hex(x) for x in packet])
        # Also read the RSSI (signal strength) of the last received message and
        # print it.
        rssi = rfm.last_rssi
        print(f"Received signal strength: {rssi} dB")
"""