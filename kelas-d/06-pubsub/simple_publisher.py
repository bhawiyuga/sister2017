import paho.mqtt.client as mqtt

# Inisiasi objek mqtt client
mqttc = mqtt.Client("pub1", clean_session=True)

# Koneksi ke broker
mqttc.connect("127.0.0.1", 1883)

# Publish
mqttc.publish("/node/1/suhu", payload="20", qos=1)
mqttc.publish("/node/1/kelembaban", payload="80", qos=1)
mqttc.publish("/node/2/suhu", payload="28", qos=1)
mqttc.publish("/node/2/kelembaban", payload="90", qos=1)