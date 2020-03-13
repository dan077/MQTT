import sys
import os.path
import configparser
from mqtt.mqtt import Mqtt

if __name__ == "__main__":

    MqttOBJ = Mqtt();

    lineCommands = sys.argv;
    lineCommandsSize = lineCommands.__len__();

    sw = False;

    if (lineCommandsSize > 1):
        if(lineCommands[1] == "--help"):
            print("*MQTT \n -> mqtt statussubscribe/publisher = 'Informacion de la configuracion'\n -> mqtt config connection subscribe/publisher ipServer xxx topic xxx = 'Cambiar los valores actuales de conexion'")

        elif (lineCommands[1] == "mqtt"):

            if (lineCommandsSize == 3):
                if (lineCommands[2] == "initSub"):
                    if(MqttOBJ.ConnectionStatus_sub()):
                        MqttOBJ.Init_subscribe()
                    else:
                        print(MqttOBJ.MessageStatus_sub())
                    sw = True;

            if (lineCommandsSize == 4):
                if (lineCommands[2] == "status" and lineCommands[3] == "subscribe"):
                    print(MqttOBJ.MessageStatus_sub())
                    sw = True;

                elif (lineCommands[2] == "status" and lineCommands[3] == "publisher"):
                    print(MqttOBJ.MessageStatus_Pub())
                    sw = True;

                elif (lineCommands[2] == "send" ):
                    if (MqttOBJ.ConnectionStatus_pub()):
                        MqttOBJ.SendMessage(lineCommands[3])
                    else:
                        print(MqttOBJ.MessageStatus_Pub())
                    sw = True;

            elif (lineCommandsSize == 9):

                if (lineCommands[2] == "config" and lineCommands[3] == "connection" and lineCommands[4] == "subscribe" and lineCommands[5] == "ipServer" and
                        lineCommands[7] == "topic"):
                    ip = lineCommands[6];
                    topic = lineCommands[8];
                    MqttOBJ.setTopic_sub(topic);
                    MqttOBJ.setServer_sub(ip);


                    print("\nNew configure Subscribe \nIp = {} \nChannel= {}".format(ip, topic));
                    sw = True;
                elif (lineCommands[2] == "config" and lineCommands[3] == "connection" and lineCommands[4] == "publisher" and lineCommands[5] == "ipServer" and
                      lineCommands[7] == "topic"):
                    ip = lineCommands[6];
                    topic = lineCommands[8];
                    MqttOBJ.setTopic_pub(topic);
                    MqttOBJ.setServer_pub(ip);

                    print("\nNew configure Publisher \nIp = {} \nChannel= {}".format(ip, topic));
                    sw = True;

    if (not sw):
        print("Error en la linea de comandos." + lineCommands[2] )
