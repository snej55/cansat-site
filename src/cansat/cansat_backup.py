import time, board, json

#from bmp280 import create_bmp280
from rfm69 import create_rfm69
#from lis3dh import *

#bmp280 = create_bmp280()
rfm = create_rfm69()
#lis3dh = create_lis3dh(board.GP3, board.GP2)

def gen_data(bmp280, lis3dh) -> str:
    data = {
        "bmp": {
            "temp": bmp280.temperature,
            "pres": bmp280.pressure,
            "alt": bmp280.altitude
        },
        "lis": {
            "acc": reading_lis3dh(lis3dh)
        }
    }
    return json.dumps(data)

#rfm.reset()
while True:
    packet = rfm.receive()
    if packet is None:
        print("Recieved nothing! Listening again...")
    else:
        print(f"Recieved raw bytes: {packet}")
        
        print(f"Received (raw bytes): {packet}")
        try:
            packet_text = str(packet, "ascii")
            print(time.time())
            print(f"Received (ASCII): {packet_text}")
        except UnicodeError:
            print("Hex data: ", [hex(x) for x in packet])
        
        rssi = rfm.last_rssi
        print(f"Received signal strength: {rssi} dB")
        
        rfm.send(bytes("REQUEST_DATA", "utf-8"))
