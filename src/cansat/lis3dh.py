"""
***** LIS3DH 3-axis accelerometer *****
"""

import board
import busio
import adafruit_lis3dh

def create_lis3dh() -> adafruit_lis3dh.LIS3DH_I2C:
    # create i2c bus
    i2c = busio.I2C(board.GP1, board.GP0)
    # create acceleromter instance
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
    # optionally set range (default is RANGE_2_G)
    #lis3dh.range = adafruit_lis3dh.RANGE_2_G
    return lis3dh