import socket
import json

# Inisiasi socket baru
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ajukan permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 6666) )

list_mahasiswa = [
	{"nama" : "Andi", "nim":"1234", "jurusan":"TiF"},
	{"nama" : "Joko", "nim":"7890", "jurusan":"TekKom"}
]

list_mahasiswa_json = json.dumps(list_mahasiswa)

# Kirim data ke server
sock.send(list_mahasiswa_json)

# Terima data dari server
data = sock.recv(1024)
print data