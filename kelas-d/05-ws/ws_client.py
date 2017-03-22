import urllib, httplib
import json

def semua_node():
	# Buat koneksi ke server
	conn = httplib.HTTPConnection('127.0.0.1:5566')
	# Kirim request GET
	conn.request('GET', '/node')
	# Ambil dan baca responsenya
	response = conn.getresponse()
	resp = response.read()
	# Print
	data_sensor = json.loads(resp)
	for i in data_sensor :
		print str(i["id"])+" "+str(i["suhu"])

def satu_node(id_node):
	# Buat koneksi ke server
	conn = httplib.HTTPConnection('127.0.0.1:5566')
	# Kirim request GET
	conn.request('GET', '/node/'+str(id_node))
	# Ambil dan baca responsenya
	response = conn.getresponse()
	resp = response.read()

	if response.status == 200 :
		# Parsing
		node = json.loads(resp)
		print str(node["id"])+" "+str(node["suhu"])
	else :
		print "Data tidak ditemukan"

#semua_node()
satu_node(2)
