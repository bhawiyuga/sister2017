import httplib, urllib
import json

def semua():
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node")
	response = conn.getresponse()
	resp = response.read()
	print resp

def satu(node_id):
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node/"+str(node_id))
	response = conn.getresponse()
	if response.status == 200 :
		resp = response.read()
		print resp
	elif response.status == 404 :
		print "Node tidak ditemukan"
	else :
		print "Error"

def create():
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	# Definisikan header content type dan accept
	headers = {"Content-type": "application/x-www-form-urlencoded", 
			"Accept": "text/plain"}
	# Definisikan body
	params = urllib.urlencode({'id': 4, 'temp' : 25, 'humidity': 60})
	# Kirim request POST dengan headet dan body
	conn.request("POST", "/node", params, headers)
	# dapatkan response nya
	response = conn.getresponse()
	print response.read()
	if response.status == 200 :
		print "Data berhasil dimasukkan"
	else :
		print "Data gagal dimasukkan"

def update(id_node):
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	# Definisikan header content type dan accept
	headers = {"Content-type": "application/x-www-form-urlencoded", 
			"Accept": "text/plain"}
	# Definisikan body
	params = urllib.urlencode({'temp' : 40, 'humidity': 80})
	# Kirim request POST dengan headet dan body
	conn.request("PUT", "/node/"+str(id_node), params, headers)
	# dapatkan response nya
	response = conn.getresponse()
	print response.read()
	if response.status == 200 :
		print "Data berhasil diupdate"
	else :
		print "Data gagal diupdate"

def delete(id_node):
	conn = httplib.HTTPConnection('127.0.0.1:7777')	
	# Kirim request POST dengan headet dan body
	conn.request("DELETE", "/node/"+str(id_node))
	# dapatkan response nya
	response = conn.getresponse()
	print response.read()
	if response.status == 200 :
		print "Data berhasil dihapus"
	else :
		print "Data gagal dihapus"

#semua()
#satu(1)
#create()
#update(4)
delete(4)