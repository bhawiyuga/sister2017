import paho.mqtt.client as mqtt

# Inisiasi objek mqtt client
mqttc = mqtt.Client("sub1", clean_session=True)

# Koneksi ke broker
mqttc.connect("127.0.0.1", 1883)

def on_message(mqttc, obj, msg):
	print "Topik "+msg.topic+" Payload "+msg.payload+" QoS "+str(msg.qos)

# Daftarkan callback function
mqttc.on_message = on_message

# Subscribe dengan topik tertentu
# mqttc.subscribe("/node/1/suhu", qos=1)

# Wildcard
#mqttc.subscribe("/node/#", qos=1)
mqttc.subscribe("/node/+/suhu", qos=1)

# Loop
mqttc.loop_forever()
