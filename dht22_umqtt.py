from umqtt.simple import MQTTClient
from machine import Pin

import btree
import time
import machine
import ujson
import esp
import network
import dht

d = dht.DHT22(machine.Pin(4))
d.measure()

mq = MQTTClient("user", "mosquitto.org", 1883, "monar", "password)
mq.connect()

while True:
    temperature = d.temperature()
    humidity = d.humidity()
    payload = ujson.dumps({
        "temperature": temperature,
        "humidity": humidity
        })
    print("Publicou")
    mq.publish(b"ifpi/lab", payload)
    time.sleep(5)
