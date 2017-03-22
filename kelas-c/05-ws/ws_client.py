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

#semua()
satu(1)