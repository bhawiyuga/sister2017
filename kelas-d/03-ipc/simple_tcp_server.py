import socket

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
	data = conn.recv(100)
	print "Menerima data "+data+" dari client"
	# Ubah datanya
	data = "OK "+data
	# Kirim balik ke client
	conn.send(data)
	# Tutup koneksi
	# conn.close()