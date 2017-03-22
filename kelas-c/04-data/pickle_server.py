import socket
import pickle
from kelas import Mahasiswa

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat IP dan port tertentu
s.bind(('', 8889))

# Listen
s.listen(10)

while True :
	# Mekanisme accept untuk 3-way handshaking
	# Return value : object koneksi conn dan address dari client
	conn, addr = s.accept()
	# Menerima data dari client
	data, sender = conn.recvfrom(100000)
	
	mahasiswa = pickle.loads(data)
	print mahasiswa.nama+" "+mahasiswa.nim

	data = "Diterima data mahasiswa"
	# Kirim ulang ke client
	conn.send(data)
	# Tutup koneksi
	conn.close()