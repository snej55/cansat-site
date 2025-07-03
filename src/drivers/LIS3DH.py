import time
import board
import busio
import adafruit_lis3dh

# Create I2C bus
i2c = busio.I2C(board.GP1, board.GP0)

# Create LIS3DH accelerometer instance
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Optionally set range (default is RANGE_2_G)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

print("LIS3DH test - I2C mode")

while True:
    x, y, z = lis3dh.acceleration
    print("X: %.2f m/s^2 \tY: %.2f m/s^2 \tZ: %.2f m/s^2" % (x, y, z))
    time.sleep(0.05)