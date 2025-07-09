import board
import busio
import digitalio
import adafruit_rfm69
import time
import json

# Create the SPI bus
spi = busio.SPI(board.GP6, board.GP7, board.GP4)  # SCK, MOSI, MISO

# Chip select and reset pins
cs = digitalio.DigitalInOut(board.GP5)
reset = digitalio.DigitalInOut(board.GP13)

# Initialize the radio
rfm = adafruit_rfm69.RFM69(spi, cs, reset, 434.0, baudrate=2000000)
encryption_key = "VB6CYeaOtduNZcgu"
rfm.encryption_key = encryption_key
rfm.tx_power = 13

print("CanSat Init")

#while True:
message = "CANSAT_RADIO_ALIVE"
station_message = "STATION_RADIO_ALIVE"


def waitUntil(statement, requirement):
    while statement != requirement:
        pass


def process_handshake(packet):
    try:
        packet_text = str(packet, "ascii")
    except UnicodeError:
        print(f"RAW HEX: {packet}")
        return 
    if packet_text == station_message:
        rssi = rfm.last_rssi
        print(f"Handshake suceeded! Signal Strength: {rssi} dB")

def wait_handshake():
    rfm.send(bytes(message, "utf-8"))
    packet = rfm.receive()
    
    if packet is None:
        print("Received nothing! Listening again...")
        return False
        
    else:
        return packet
    
while True: #Busy wait for station to respond
    packet = wait_handshake()
    if packet != False:
        process_handshake(packet)
        rfm.send(bytes(message, "utf-8"))
        break