import time

from bmp280 import create_bmp280
from rfm69 import create_rfm69

bmp280 = create_bmp280()
rfm = create_rfm69()

while True:
    log = f"Temp: {bmp280.temperature :.2f} C, Pressure: {bmp280.pressure :.2f} hPa, Altitude: {bmp280.altitude :.2f}"
    print(log)
    rfm.send(bytes(log, "utf-8"))
    time.sleep(0.5)