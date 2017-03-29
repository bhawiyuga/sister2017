from flask import Flask, abort, request, Response, make_response
import json

app = Flask(__name__)

list_node = [
		{"id":1, "suhu":30, "kelembaban":80},
		{"id":2, "suhu":28, "kelembaban":70}
	]

@app.route('/node', methods=['GET'])
def semua():
	return json.dumps(list_node)

@app.route('/node/<int:id_node>', methods=['GET'])
def satu(id_node):
	node = None
	# Iterasi data tiap node yang ada di list
	for n in list_node :
		if n["id"] == id_node:
			node = n
	# Cek apakah node tersebut ditemukan
	if node is None :
		return "Node tidak ditemukan", 404
	else :
		return json.dumps(node)

@app.route('/node', methods=['POST'])
def create():
	# Tangkap semua parameter dari body-nya request
	id_node = request.form["id"]
	suhu = request.form["suhu"]
	kelembaban = request.form["kelembaban"]
	# Buat object dictionary baru
	node_baru = {"id" : int(id_node), "suhu" : int(suhu), "kelembaban" : int(kelembaban)}
	# Masukkan object dictionary baru ke list
	list_node.append(node_baru)
	# Return data node baru
	return json.dumps(node_baru) 

@app.route('/node/<int:id_node>', methods=['PUT'])
def update(id_node):
	# Cari data yang akan diupdate
	node = None
	# Iterasi data tiap node yang ada di list
	for n in list_node :
		if n["id"] == id_node:
			node = n
	# Cek apakah node tersebut ditemukan
	if node is None :
		return "Node tidak ditemukan", 404
	else :
		# Ambil parameter dari body-nya request
		suhu = request.form["suhu"]
		kelembaban = request.form["kelembaban"]
		# Ubah nilai dari node yang sudah ditemukan
		node["suhu"] =  int(suhu)
		node["kelembaban"] = int(kelembaban)
		# Response
		return json.dumps(node)

@app.route('/node/<int:id_node>', methods=['DELETE'])
def delete(id_node):
	# Cari data yang akan diupdate
	node = None
	# Iterasi data tiap node yang ada di list
	for n in list_node :
		if n["id"] == id_node:
			node = n
	# Cek apakah node tersebut ditemukan
	if node is None :
		return "Node tidak ditemukan", 404
	else :
		# Hapus node yg ditemukan dari list
		list_node.remove(node)
		# Response
		return "OK"


app.run(debug=True, port=5566)
