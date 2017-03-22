from flask import Flask

# Inisialisasi app Flask
app = Flask(__name__)

# Definisikan fungsi untuk menghandle request
@app.route('/node', methods=['GET'])
def hello():
	return "Hello world"

# Definisikan fungsi untuk menghandle request
@app.route('/mahasiswa', methods=['GET'])
def mahasiswa():
	return "Joko"

# Run apps
app.run(debug=True, port=5577)