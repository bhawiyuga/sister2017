from flask import Flask, abort, request
import json

app = Flask(__name__)

list_node = [{"id": 1, "temp": 37, "humidity" : 70},
			{"id": 2, "temp": 40, "humidity" : 80}]


@app.route('/node', methods=['GET'])
def semua():
	return json.dumps(list_node)

@app.route('/node/<int:node_id>', methods=['GET'])
def satu(node_id):
	node = None
	for n in list_node :
		if n["id"] == node_id :
			node = n
	if node :
		return json.dumps(node)
	else :
		abort(404)

@app.route('/node', methods=['POST'])
def create():
	# Ambil data ID
	id_node = request.form["id"]
	# Ambil data suhu
	suhu = request.form["temp"]
	# Ambil data kelembaban
	kelembaban = request.form["humidity"]
	# Buat node baru
	node_baru = {"id" : int(id_node), "temp": int(suhu), "humidity": int(kelembaban)}
	# Tambahkan node baru ke list_node
	list_node.append(node_baru)
	# return
	return "OK"

@app.route('/node/<int:id_node>', methods=['PUT'])
def update(id_node):
	# Ambil data suhu
	suhu = request.form["temp"]
	# Ambil data kelembaban
	kelembaban = request.form["humidity"]
	# Cari node terlebih dahulu
	node = None
	for n in list_node :
		if n["id"] == id_node :
			node = n
	# Jika tidak ada, return 404
	if node is None :
		abort(404)
	# Jika ada, update isinya
	else :
		node["temp"] = int(suhu)
		node["humidity"] = int(kelembaban)
	# return
	return "OK"

@app.route('/node/<int:id_node>', methods=['DELETE'])
def delete(id_node):
	node = None
	for n in list_node :
		if n["id"] == id_node :
			node = n
	# Jika tidak ada, return 404
	if node is None :
		abort(404)
	# Jika ada, hapus node-nya
	else :
		list_node.remove(node)
	return "OK"


if __name__=='__main__':
	app.run(debug=True, port=7777)
