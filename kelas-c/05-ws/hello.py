from flask import Flask

# Inisiasi app Flask
app = Flask(__name__)

@app.route('/node', methods=['GET'])
def hello():
	return "Hello world"

@app.route('/mahasiswa', methods=['GET'])
def mahasiswa():
	return "Joko"

if __name__ == '__main__':
	app.run(debug=True)