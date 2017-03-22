import socket
import pickle
from mahasiswa import Mahasiswa

# Inisiasi object socket TCP/IPv4
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind
sock.bind( ('', 6666) )

# Listen
sock.listen(10)

while True:
	# Accept permintaan 3-way handshaking
	conn, address = sock.accept()
	# Terima data dari client
	data = conn.recv(1024)
	print data
	# Unmarshall
	mahasiswa = pickle.loads(data)

	kembalian = "Nama mahasiswa 1 "+mahasiswa.nama
	print kembalian
	# Ubah datanya
	data = "OK "+kembalian
	# Kirim balik ke client
	conn.send(data)
	# Tutup koneksi
	# conn.close()