#!usr/bin/#!/usr/bin/python3
import paho.mqtt.client as paho #mqtt library


#host name is localhost because both SERVIDOR and python are Running on same
#machine/Computer.

PUERTO = 1883 #MQTT data listening port

#ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j' #not manditory


def on_publish(client,userdata,result): #create function for callback
  print("Mensaje enviado...\n")
  pass

def ConfigurePublisher(ipServer):
    client1 = paho.Client()  # create client object
    client1.on_publish = on_publish  # assign function to callback
    # client1.username_pw_set(ACCESS_TOKEN) #access token from thingsboard device
    client1.connect(ipServer, PUERTO, keepalive=45)  # establishing connection
    return client1;

def sendMessage(message,ipServer,topic):
    config = ConfigurePublisher(ipServer);
    config.publish(topic, message)
    #print("Mensaje enviado...\n")

