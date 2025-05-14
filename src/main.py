from machine import Pin, I2C
from bmp280 import *
import time

class CanSat:
    def __init__(self):
        self.bmp = None
        init_bmp()
    
    # initialize BMP280
    def init_bmp(self, sda_pin, scl_pin):
        # create the i2c bus
        bus = I2C(0, sda=sda_pin, scl=scl_pin, freq=19000)
        # give it some time
        time.sleep(0.1)
        # create bmp
        bmp = BMP280(bus)
    
    # get temperature from bmp in celsius
    def get_temperature():
        return bmp.temperature
    
    # get pressure in Pa
    def get_pressure():
        return bmp.pressure
    
    # get pressure from bmp in bar
    def get_pressure_bar():
        pressure = bmp.pressure
        # convert from Pa to bar
        return pressure / 100000
        
if __name__ == "__main__":
    cansat = CanSat()
    while True:
        print(f"Temperature: {cansat.get_temperature()} C")
        print(f"Pressure: {cansat.get_pressure()} Pa | {cansat.get_pressure_bar} bar")
        time.sleep(0.5)

# sda_pin = machine.Pin(0)
# scl_pin = machine.Pin(1)
# bus = I2C(0, sda=sda_pin, scl=scl_pin, freq=19000)
# time.sleep(0.1)
# bmp = BMP280(bus)

# bmp.use_case(BMP280_CASE_INDOOR)

# while True:
#     pressure = bmp.pressure
#     p_bar = pressure / 100000 # convert to bar (1000 kPa)
#     temperature = bmp.temperature
#     print(f"Temperature: {temperature} C")
#     print(f"Pressure: {pressure} Pa | {p_bar} bar")
#     time.sleep(0.5)
    