from machine import Pin, I2C
from bmp280 import *
import time

class CanSat:
    def __init__(self):
        self.bmp = None
        self.init_bmp(0, 1)
    
    # initialize BMP280
    def init_bmp(self, sda_pin, scl_pin):
        # create the i2c bus
        bus = I2C(0, sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin), freq=19000)
        # give it some time
        time.sleep(0.1)
        # create bmp
        self.bmp = BMP280(bus)
    
    # get temperature from bmp280 in celsius
    def get_temperature_bmp(self):
        return self.bmp.temperature
    
    # get pressure in Pa
    def get_pressure_bmp(self):
        return self.bmp.pressure
    
    # get pressure from bmp in bar
    def get_pressure_bar_bmp(self):
        pressure = self.bmp.pressure
        # convert from Pa to bar
        return pressure / 100000
        
if __name__ == "__main__":
    cansat = CanSat()
    while True:
        print(f"Temperature: {cansat.get_temperature_bmp()} C")
        print(f"Pressure: {cansat.get_pressure_bmp()} Pa | {cansat.get_pressure_bar_bmp()} bar")
        time.sleep(0.5)

