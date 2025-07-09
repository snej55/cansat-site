import board
import busio
import digitalio
import adafruit_rfm69
import time
#import adafruit_bmp280

#sda = board.GP0
#scl = board.GP1
#i2c = busio.I2C(scl=scl, sda=sda)
#bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
#bmp280.sea_level_pressure = bmp280.pressure # relative pressure

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

while True:
    rfm.send(bytes("sssssssssssssssssssssssssssssssssssssssssssssssssss", "utf-8"))
    time.sleep(0.5)
    print("sssssssssssssssssssssssssssssssssssssssssssssssssss")