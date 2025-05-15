import machine
import time

buzzer = machine.PWM(machine.Pin(15)) # Assign the PWM to pin 15

led = machine.Pin("LED", machine.Pin.OUT)

def landed():
    buzzer.freq(2220)
    while True:
        led.off()
        buzzer.duty_u16(0)
        time.sleep(0.5)
        led.on()
        buzzer.duty_u16(500) # Change the duty cycle for volume control 0 to 32767, anythink higher will damage the buzzer
        time.sleep(0.5)

# time.sleep(5)
landed()

