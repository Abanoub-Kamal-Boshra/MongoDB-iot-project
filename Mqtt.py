from paho.mqtt import client as mqtt_client
import json
from MongoDB import clusterUrl,connectToMongoClient,writeOnDatabase

mqttBroker ="broker.emqx.io"
port = 1883
topic = "/python/mqtt/temp"

atlasClient = connectToMongoClient(clusterUrl)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client("Python Code")#(client_id)
    #overriding (method can i use in python as originaly there is no overriding in python)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(mqttBroker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #msg.payload.decode() --> to print the origin message
        studentDocument = msg.payload.decode()
        #convert str to dict
        studentDocument = json.loads(studentDocument) 
        #write on atlas
        id = writeOnDatabase(atlasClient, 'ITI_IoT_DB', studentDocument)
        # print(id)
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def getData(studentDocument):
    return studentDocument

def run():
    client = connect_mqtt()
    subscribe(client) #stay listen on the client
    client.loop_forever()

if __name__ == '__main__':
    run()