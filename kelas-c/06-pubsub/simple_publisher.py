# Import library paho-mqtt
import paho.mqtt.client as mqtt

# Inisiasi object mqtt
mqttc = mqtt.Client("pub1", clean_session=True)

# Buat koneksi ke broker
mqttc.connect( "127.0.0.1", 1883 )

# Publish
mqttc.publish("/node/1/suhu", payload="12", qos=1)
mqttc.publish("/node/1/kelembaban", payload="80", qos=1)
mqttc.publish("/node/2/suhu", payload="20", qos=1)
mqttc.publish("/node/2/kelembaban", payload="90", qos=1)