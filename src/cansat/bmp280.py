"""
***** BMP280 Pressure sensor *****
"""
import board
import busio
import adafruit_bmp280

# pressure sensor
def create_bmp280() -> adafruit_bmp280.Adafruit_BMP280_I2C:
    sda = board.GP0
    scl = board.GP1
    i2c = busio.I2C(scl=scl, sda=sda)
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
    bmp280.sea_level_pressure = bmp280.pressure # relative pressure
    return bmp280