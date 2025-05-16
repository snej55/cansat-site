import machine
import time
import MPU6050
import sys


# Set up the I2C interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))

# Set up the MPU6050 class
mpu = MPU6050.MPU6050(i2c)

# wake up the MPU6050 from sleep
mpu.wake()

mpu.write_lpf_range(6)  # reduce noise

while True:
    x_accel, y_accel, z_accel = mpu.read_accel_data() # Outputs the acceleration raw data in g

    temp = mpu.read_temperature()


    
    data_sent = mpu.read_accel_data() + (temp, )

    print(data_sent)
  


    #print(temp)
    time.sleep(0.1)



