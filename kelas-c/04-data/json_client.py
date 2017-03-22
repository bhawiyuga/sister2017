import socket
import json

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bikin koneksi ke server (3-way handshaking)
s.connect(('127.0.0.1', 8889))

data_mahasiswa = [
{"nama" : "Andi", "nim":"12345", "jurusan":"TekKom"},
{"nama" : "Joko", "nim" : "7890", "jurusan": "TIF"}
]

#print data_mahasiswa[0]["nama"]+" "+data_mahasiswa[0]["jurusan"]
mahasiswa_str = json.dumps(data_mahasiswa)
#print mahasiswa_str

# Kirim data
s.send(mahasiswa_str)
# Terima balasan dari server
data = s.recv(100000)
# Cetak balasan dari server
print data
# Tutup koneksi
s.close()