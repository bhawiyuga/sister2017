import socket

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
	data, sender = conn.recvfrom(100)
	print "Menerima data "+data+" dari client"
	# Data tambah string OK
	data = "OK "+data
	# Kirim ulang ke client
	conn.send(data)
	# Tutup koneksi
	conn.close()