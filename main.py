import paho.mqtt.client as mqtt
import time
import random

BROKER = "test.mosquitto.org"
TOPIC = "factory/machine1/temp"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temp = round(random.uniform(20, 80), 2)

    payload = f"{temp}"
    client.publish(TOPIC, payload)

    print(f"Sent: {payload} °C")
    time.sleep(2)
