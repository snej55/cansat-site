import time, board, json, busio, digitalio, adafruit_rfm69

#from bmp280 import create_bmp280
from rfm69 import create_rfm69
#from lis3dh import *

class Cansat:
    def __init__(self):
        self.rfm = self.create_rfm69(board.GP6, board.GP7, board.GP4, board.GP5, board.GP13)
        self.data_type = "NONE"
        self.status = "LISTENING"
    
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
    
    def gen_data(self) -> str:
        if self.data_type == "NONE":
            return "garbage"
        elif self.data_type == "BMP":
            return "some pressure data"
        else:
            return "hot garbage"
    
    def process_packet(self, packet_text) -> str:
        # discard if text is invalid
        if packet_text == "STATUS_ERROR":
            self.status = "LISTENING"
            return
        
        if packet_text == "REQUEST_DATA":
            self.status = "REQUEST_DATA"
            return
        
        if packet_text == "DATA_TYPE":
            self.status = "RECIEVE_DATA_TYPE"
            return
        
        if self.status == "RECIEVE_DATA_TYPE":
            self.data_type = packet_text
            self.status = "SET_DATA_TYPE"
            return

        if packet_text == "SEND_DATA":
            self.status = self.gen_data() # dummy data
            return

        if packet_text == "STATUS":
            self.status = "SUCCESS"
            return
        
        if packet_text == "EXIT_SUCCESS":
            self.status = "LISTENING"
            return
    
    def broadcast(self):
        while True:
            self.rfm.send(bytes(self.status, "utf-8"))
            packet = self.rfm.receive()
            if packet is None:
                print("Recieved nothing! Listening again...")
            else:
                packet_text = self.process_data(packet)
                rssi = self.rfm.last_rssi
                print(f"Recieved signal strength: {rssi} dB")

                self.process_packet(packet_text)
                print(f"Recieved packet: {packet_text}")
                print(f"STATUS: {self.status}")


cansat = Cansat()
cansat.broadcast()