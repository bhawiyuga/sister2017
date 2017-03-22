import socket
from thread import start_new_thread

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat IP dan port tertentu
s.bind(('', 8887))

# Listen
s.listen(10)

def client_thread(conn):
	while True :
		# Menerima data dari client
		data, sender = conn.recvfrom(100)
		print "Menerima data "+data+" dari client"
		# Data tambah string OK
		data = "OK "+data
		# Kirim ulang ke client
		conn.send(data)
		# Tutup koneksi
	conn.close()

while True :
	# Mekanisme accept untuk 3-way handshaking
	# Return value : object koneksi conn dan address dari client
	conn, addr = s.accept()
	start_new_thread(client_thread, (conn,))
	