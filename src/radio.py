import time

pin16 
pin17

def transmit(data):
    pin17 = data
    pin16 = True
    time.sleep(0.00001)
    pin16 = False

transmit(True)