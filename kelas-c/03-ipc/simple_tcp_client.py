import socket

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bikin koneksi ke server (3-way handshaking)
s.connect(('127.0.0.1', 8887))
while True :
	data = raw_input("Masukkan data yang akan dikirim : ")
	# Kirim data
	s.send(data)
	# Terima balasan dari server
	data = s.recv(100)
	# Cetak balasan dari server
	print data
# Tutup koneksi
s.close()