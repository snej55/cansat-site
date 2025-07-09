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

print("CanSat Ground Station Init")

while True:
    
    #time.sleep(1)
    #print("Waiting for packets...")
    rfm.send(bytes("qwertyuioplkjhgfdsazxcv" * 2,"utf-8"))
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