import wifi
import sensor
import lora
import time
from network import LoRa


LoRa = lora.init()
print("LoRa")
if not LoRa.has_joined():
    wifi.set_connect()
    print("wifi")

sensor.defsensor()
print("sensor")
while True:

    distance = sensor.getdistance()
    if not LoRa.has_joined():
        wifi.send(distance)
    else:
        lora.send(distance)
    time.sleep(10)
