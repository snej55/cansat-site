"""
***** LIS3DH 3-axis accelerometer *****
https://docs.circuitpython.org/projects/lis3dh/en/latest/api.html
"""

import board
import busio
import adafruit_lis3dh

def create_lis3dh(sda,scl):

    # create i2c bus
    # Create I2C bus
    i2c = busio.I2C(sda, scl)

    # Create LIS3DH accelerometer instance
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
    # optionally set range (default is RANGE_2_G)
    #lis3dh.range = adafruit_lis3dh.RANGE_2_G
    return lis3dh
def reading_lis3dh(lis3dh):
    
    acc_x, acc_y, acc_z = lis3dh.acceleration
    return [acc_x,acc_y,acc_z]

lis3dh = create_lis3dh(board.GP1, board.GP0)
print(reading_lis3dh(lis3dh))