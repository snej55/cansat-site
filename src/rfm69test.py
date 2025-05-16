import time
import board
import busio
import digitalio


import adafruit_rfm69

# basic on board led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False  # turn off led



# radio
FREQ = 433.0
spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP0)
cs = digitalio.DigitalInOut(board.GP1)
reset = digitalio.DigitalInOut(board.GP4)
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, FREQ)

# uncomment to enable encryption
# rfm69.encryption_key = (
#     b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
# )

listen = False
count = 0
msg = ''
while True:

    if not listen:
        if button_left.value:
            FREQ = round(FREQ + 0.1, 1)
            rfm69.frequency_mhz = FREQ

        if button_right.value:
            FREQ = round(FREQ - 0.1, 1)
            rfm69.frequency_mhz = FREQ


            led.value = True



    if listen:
        packet = rfm69.receive()
        if packet is not None:
            packet_text = str(packet, 'ascii')
            msg = packet_text
            print('Received: {0}'.format(packet_text))
            count = count + 1