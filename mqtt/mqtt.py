import os.path
import configparser
from .sub import Subscribe
from .pub import sendMessage

class Mqtt:
    def __init__(self):
        self.name = "mqttConfig";
        if (not os.path.isfile(self.name+'.ini')):
            self.CreateConfig();

        self.serverTopic_sub = [];
        self.serverTopic_pub = [];


        #add values to serverTopic_sub
        self.serverTopic_sub.append(self.getValueConfig("Subscribe", "IpServer"));
        self.serverTopic_sub.append(self.getValueConfig( "Subscribe", "Topic"));

        #add values to ServerTopic_pub
        self.serverTopic_pub.append(self.getValueConfig( "Publisher", "IpServer"));
        self.serverTopic_pub.append(self.getValueConfig("Publisher", "Topic"));

    #method
    def Init_subscribe(self):
        Subscribe(self.serverTopic_sub[0],self.serverTopic_sub[1]);

    def SendMessage(self,Message):
        sendMessage(Message,self.serverTopic_pub[0],self.serverTopic_pub[1])

    def ConnectionStatus_sub(self):
        if(self.serverTopic_sub[0] == "NULL" or self.serverTopic_sub[1] == "NULL" ):
            return False;
        return True;

    def ConnectionStatus_pub(self):
        if(self.serverTopic_pub[0] == "NULL" or self.serverTopic_pub[1] == "NULL" ):
            return False;
        return True;

    def MessageStatus_Pub(self):
        Message = "La conexion del Publisher está: "
        Message += "Sin configurar" if self.ConnectionStatus_pub() else "Configurada";
        return Message;

    def MessageStatus_sub(self):
        Message = "La conexion del Subscribe está: "
        Message += "Sin configurar" if self.ConnectionStatus_sub() else "Configurada";
        return Message;

    #Set & get suscribe.
    def getServer_sub(self):
        return self.serverTopic_sub[0];

    def setServer_sub(self,newValue):
        self.ModifyConfig("Subscribe","IpServer",newValue);
        self.serverTopic_sub[0] = newValue;

    def getTopic_sub(self):
        return self.serverTopic_sub[1];

    def setTopic_sub(self,newValue):
        self.ModifyConfig("Subscribe","Topic",newValue);
        self.serverTopic_sub[1] = newValue;
    #end

    #set & get publisher
    def getServer_pub(self):
        return self.serverTopic_pub[0];

    def setServer_pub(self,newValue):
        self.ModifyConfig("Publisher","IpServer",newValue);
        self.serverTopic_pub[0] = newValue;

    def getTopic_pub(self):
        return self.serverTopic_pub[1];

    def setTopic_pub(self,newValue):
        self.ModifyConfig("Publisher","Topic",newValue);
        self.serverTopic_pub[1] = newValue;

    #end

    #Manage File
    def CreateConfig(self,name):
        config = configparser.ConfigParser();
        config.add_section("Subscribe");
        config.set("Subscribe", "IpServer", "NULL");
        config.set("Subscribe", "Topic", "NULL");
        config.add_section("Publisher");
        config.set("Publisher", "IpServer", "NULL");
        config.set("Publisher", "Topic", "NULL");

        with open(self.name + '.ini', 'w') as config_file:
            config.write(config_file);

    def ModifyConfig(self, section, option, newValue):
        config = configparser.ConfigParser();
        config.read(self.name + ".ini")
        config.set(section, option, newValue);
        with open(self.name + '.ini', 'w') as config_file:
            config.write(config_file);


    def getValueConfig(self, section, option):
        config = configparser.ConfigParser();
        config.read(self.name + ".ini")
        return config.get(section, option);







