"""
A basic class for our CanSat, with interfaces for our different sensors.
It uses the BMP280 for temperature and pressure, and the MPU6050 for acceleration and gyro axis.
It also has support for an SSD1306 OLED screen, and a pwm buzzer.
"""

from machine import Pin, I2C
from bmp280 import *
import MPU6050
import time

# oled screen
from ssd1306 import SSD1306_I2C

class CanSat:
    def __init__(self):
        # bmp280
        self.bmp = None
        self.init_bmp(0, 1)
        
        # base pressure
        self.base_pressure = 102325
        
        # mpu6050
        self.mpu = None
        self.init_mpu(None)
        
        # oled screen
        self.width = 128
        self.height = 64
        self.oled = None
        #self.init_oled(3, 2)
        
        # buzzer
        self.buzzer = None
        self.init_buzzer()

    # ----- BMP280 ------ #

    # initialize BMP280
    def init_bmp(self, sda_pin, scl_pin):
        # create the i2c bus
        bus = I2C(0, sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin), freq=19000)
        # give it some time
        time.sleep(0.1)
        # create bmp
        self.bmp = BMP280(bus)
        
    def init_mpu(self, i2c):
        self.mpu = MPU6050.MPU6050(i2c)

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

    def get_altitude_bmp(self):
        pressure = self.get_pressure_bmp()
        # use barometric equation to estimate altitude
        return self.get_altitude_from_pressure(pressure)
    
    def get_altitude_from_pressure(self, pressure):
        altitude = 44330 * (1 - (pressure / self.base_pressure) ** (1 / 5.5255))
        return altitude
    
    def calibrate_pressure(self, trials=5, tick=0.5):
        pressures = []
        for i in range(trials):
            pressures.append(self.get_pressure_bmp())
            time.sleep(tick)
        self.base_pressure = sum(pressures) / len(pressures)
    
    # ------ MPU6050 ------ #
    
    # Sleep the MPU6050
    def sleep_mpu(self):
        self.mpu.sleep()
    
    # Print the gyro data to a 3-object (x,y,z)
    def get_gyro_data_mpu(self):
        return self.mpu.read_gyro_data()
    
    # Print the accelerometer data to a 3-object tuple (x,y,z)
    def get_accel_data_mpu(self):
        return self.mpu.read_accel_data()
    
    # Print the temperature in Celsius as a float
    def get_temp_data_mpu(self):
        return self.mpu.read_temperature()
    
    # ----- SSD1306 ----- #
    
    # initialize oled screen
    def init_oled(self, sda_pin, scl_pin):
        bus = I2C(0, sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin), freq=19000)
        self.oled = SSD1306_I2C(self.width, self.height, bus)
        
    # ----- Buzzer ----- #
    def init_buzzer(self):
        self.buzzer = machine.PWM(machine.Pin(15))
    
    # set the frequency for the buzzer
    def set_buzzer_freq(self, freq):
        self.buzzer.freq(freq)
    
    # set the volume for the buzzer (range 0-32_767)
    def set_buzzer_volume(self, volume):
        volume = min(32767, max(0, volume))
        self.buzzer.duty_u16(volume)

if __name__ == "__main__":
    cansat = CanSat()
    cansat.set_buzzer_freq(2220)
    pressures = []
    while True:
        print(f"Temperature: {cansat.get_temperature_bmp()} C")
        # keep track of last five pressure readings
        pressures.append(cansat.get_pressure_bmp())
        if len(pressures) > 5:
            pressures.pop(0)
        # real pressure for comparison
        real_pressure = cansat.get_pressure_bmp()
        # calculate weighted average for pressures
        average_pressure = (sum(pressures) + real_pressure) / (len(pressures) + 1)
        print(f"Pressure: {average_pressure} Pa (average) {real_pressure} Pa (real) | {cansat.get_pressure_bar_bmp()} bar")
        print(f"Altitude: {cansat.get_altitude_from_pressure(average_pressure) :.2f} m")
        time.sleep(0.5)
        if (cansat.get_altitude_bmp() > 3):
            cansat.set_buzzer_volume(2000)
        else:
            cansat.set_buzzer_volume(0)

