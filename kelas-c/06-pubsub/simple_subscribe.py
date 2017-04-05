# Import library paho-mqtt
import paho.mqtt.client as mqtt

# Inisiasi object mqtt
mqttc = mqtt.Client("sub1", clean_session=True)

# Buat koneksi ke broker
mqttc.connect( "127.0.0.1", 1883 )

def on_connect(mqttc, obj, flags, rc):
	print("Connected")

def on_message(mqttc, obj, msg):
	print "Topik "+msg.topic+" Payload : "+msg.payload+ " QoS "+str(msg.qos)

# Set callback function
mqttc.on_connect = on_connect
mqttc.on_message = on_message


# Subscribe ke topik tertentu
mqttc.subscribe("/node/+/suhu", qos=1)

# Loop supaya subscribernya tidak berhenti
mqttc.loop_forever()