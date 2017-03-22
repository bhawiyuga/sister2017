from flask import Flask, abort
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
		abort(404)
	else :
		return json.dumps(node)

app.run(debug=True, port=5566)
