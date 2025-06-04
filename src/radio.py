import time
import machine

pin16 = r.gpio16
pin17 = r.gpio16

def transmit(data):
    pin17 = data
    pin16 = True
    time.sleep(0.00001)
    pin16 = False

transmit(True)