import dht
import machine
d = dht.DHT11(machine.Pin(1))

d.measure()
print(d.humidity()," ",d.temperature())
