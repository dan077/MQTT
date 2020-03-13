#!usr/bin/#!/usr/bin/python3
from .procesamiento import send
import paho.mqtt.client as paho
import mysql.connector
import json

PUERTO = 1883

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    mensaje = send(str(msg.payload)[2:-1])
    if(mensaje != "ok"):
        print("Enviar señal de Error: " + mensaje)
    else:
        print("Se envió")

def Subscribe(ipServer,topic):
    client = paho.Client()
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.connect(ipServer, PUERTO)
    client.subscribe(topic, qos=1)
    client.loop_forever()



