import paho.mqtt.client as mqttc


# The callback for when the client receives a CONNACK response from the server.
import paho


def on_connect(mc, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mc.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(mc, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqttc.Client()
mc = paho.mqtt.client.Mosquitto("12")
mc.on_connect = on_connect
mc.on_message = on_message

mc.connect("localhost")


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mc.loop_forever()