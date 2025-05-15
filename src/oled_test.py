from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

WIDTH =128 
HEIGHT = 64
i2c=I2C(0, scl=Pin(9), sda=Pin(8), freq=19000)
oled = SSD1306_I2C(WIDTH,HEIGHT, i2c)
while True:
    oled.fill(0)
    oled.text("Hello world!", 0, 40)
    oled.show()
    time.sleep(1/30)