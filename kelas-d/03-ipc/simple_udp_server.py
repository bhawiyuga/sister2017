import socket

#Inisiasi object socket UDP/ipv4
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Binding ke sebuah port 
sock.bind( ('', 7777) )

# Buat servernya jalan terus
while True:
	# Baca data yang dikirimkan client
	data, address = sock.recvfrom(100)
	print "Menerima data "+data+" dari client"
	# Tambahkan string OK di depan data yang diterima
	data = "OK "+data
	# Kirim balik data ke client
	sock.sendto(data, address)
