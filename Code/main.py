from machine import Pin, I2C
from bmp280 import *
import time

sda_pin = machine.Pin(0)
scl_pin = machine.Pin(1)
bus = I2C(0, sda=sda_pin, scl=scl_pin, freq=19000)
time.sleep(0.1)
bmp = BMP280(bus)

bmp.use_case(BMP280_CASE_INDOOR)

while True:
    pressure = bmp.pressure
    p_bar = pressure / 100000 # convert to bar (1000 kPa)
    temperature = bmp.temperature
    print(f"Temperature: {temperature} C")
    print(f"Pressure: {pressure} Pa | {p_bar} bar")
    time.sleep(0.5)
    