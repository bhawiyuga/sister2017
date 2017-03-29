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

def create_node():
	# Buat koneksi ke server
	conn = httplib.HTTPConnection('127.0.0.1:5566')
	# Definisikan header content type dan accept
	headers = {"Content-type": "application/x-www-form-urlencoded", 
			"Accept": "text/plain"}
	# Definisikan body
	params = urllib.urlencode({'id': 3, 'suhu' : 25, 'kelembaban': 60})
	# Kirim request
	conn.request('POST', '/node', params, headers)
	# Ambil response
	response = conn.getresponse()
	resp = response.read()
	if response.status == 200 :
		print "Tambah data berhasil"
	else :
		print "Tambah data gagal"

def update_node(id_node):
	# Buat koneksi ke server
	conn = httplib.HTTPConnection('127.0.0.1:5566')
	# Definisikan header content type dan accept
	headers = {"Content-type": "application/x-www-form-urlencoded", 
			"Accept": "text/plain"}
	# Definisikan body
	params = urllib.urlencode({ 'suhu' : 100, 'kelembaban': 100})
	# Kirim request
	conn.request('PUT', '/node/'+str(id_node), params, headers)
	# Ambil response
	response = conn.getresponse()
	resp = response.read()
	if response.status == 200 :
		print "Update data berhasil"
	else :
		print "Update data gagal"

def hapus_node(id_node):
	# Buat koneksi ke server
	conn = httplib.HTTPConnection('127.0.0.1:5566')
	# Kirim request
	conn.request('DELETE', '/node/'+str(id_node))
	# Ambil response
	response = conn.getresponse()
	resp = response.read()
	if response.status == 200 :
		print "Hapus data berhasil"
	else :
		print "Hapus data gagal"

hapus_node(10)
#update_node(2)
#create_node()
#semua_node()
#satu_node(2)
