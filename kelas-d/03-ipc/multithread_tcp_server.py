import socket
from thread import start_new_thread

# Inisiasi object socket TCP/IPv4
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 6666) )

# Listen
sock.listen(10)

# Fungsi yang akan dieksekusi oleh tiap thread
def handle_connection(conn):
	try :
		while True :
			# Terima data dari client
			data = conn.recv(100)
			print "Menerima data "+data+" dari client"
			# Ubah datanya
			data = "OK "+data
			# Kirim balik ke client
			conn.send(data)
	except socket.error, e :
		print "Koneksi diputus oleh client"
		# Tutup koneksi
		conn.close()

while True:
	# Accept permintaan 3-way handshaking
	conn, address = sock.accept()
	# Buat thread baru
	start_new_thread(handle_connection, (conn,))
	