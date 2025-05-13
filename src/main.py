from picozero import pico_led
import time

while 1:
    pico_led.on()
    time.sleep(0.5)
    pico_led.off()
    time.sleep(0.5)