import time, board, json

#from bmp280 import create_bmp280
from rfm69 import create_rfm69
#from lis3dh import *

#bmp280 = create_bmp280()
rfm = create_rfm69()
#lis3dh = create_lis3dh(board.GP3, board.GP2)

def gen_pressure_data():
    data = {
        "bmp": {
            "temp": 27.6,
            "pres": 1080,
            "alt": 820
        },
    }
    return str(json.dumps(data))

def process_data(raw_packet):
    try:
        packet_text = str(raw_packet, "ascii")
        print(f"Recieved (ASCII): {packet_text}")
    
        return packet_text
    except UnicodeError:
        print(f"ERROR decoding (ASCII) data! HEX: {[hex(x) for x in raw_packet]}")
        return "STATUS_ERROR"
    
def process_packet(packet_text, status, data_type) -> str:
        # discard if text is invalid
        if packet_text == "STATUS_ERROR":
            return status
        
        if packet_text == "receive_data":
            return "receive_data"
        
        if packet_text == data_type:
            
            return data_type
        
        if packet_text == "REQUEST_DATA":
            return gen_data()
        # if it isn't any of the other stuff
        if packet_text == "STATUS":
            return "SUCCESS"
        if packet_text == "REQUEST_PRESSURE_DATA":
            return send_data("pressure")
            
        return status, data_type


# data type is type of sensor data (e.g. pressure, altitude, etc)

def send_data(datatype):
    if datatype == "pressure":
        data = gen_pressure_data()
        return data
        
    
def receive_data():
    status = "NONE"
    data_type = "NONE"
    running = True
    while running:
        rfm.send(bytes(status, "utf-8"))
        packet = rfm.receive()
        if packet is None:
            pass
            #print("Recieved nothing! Listening again...")
        else:
            packet_text = process_data(packet)
            rssi = rfm.last_rssi
            print(f"Recieved signal strength: {rssi} dB")
            
            status = process_packet(packet_text, status, data_type)



receive_data("pressure")