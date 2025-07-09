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

print("Ground Station Init")

#while True:
message = "STATION_RADIO_ALIVE"
rfm.send(bytes(message, "utf-8"))


while True: #Busy wait for cansat to respond
    packet = rfm.receive()
    if packet is None:
        print("Received nothing! Listening again...")
        
        break

def process_handshake(packet):
    packet_text = str(packet, "ascii")
    if packet_text == "CANSAT_RADIO_ALIVE":
        print("Handshake suceeded !")


    rssi = rfm.last_rssi
    print(f"Received signal strength: {rssi} dB")
