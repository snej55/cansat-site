import serial
import ast

# Specify the serial port and baud rate
serial_port = '/dev/tty.usbmodem2101'  # Replace with your device
baud_rate = 9600  # Match this to your device's settings

ser = serial.Serial(serial_port, baud_rate, timeout=1)
# Open the serial port

#Pre declare variables
x_accel, y_accel, z_accel, mpu_temp= 0, 0, 0, 0 # Declar variables(MPU6050)

def phrase_accel(raw_data):
    global x_accel, y_accel, z_accel, mpu_temp
    try:
        raw_data = ast.literal_eval(raw_data)
    except SyntaxError:
        pass
    x_accel, y_accel, z_accel, mpu_temp = raw_data


while True:
    # Read a line from the serial port
    line = ser.readline().decode('utf-8').strip()

    phrase_accel(line)
    if line:
        print(f"Received: {x_accel}, {y_accel}, {z_accel}, {mpu_temp}C")

