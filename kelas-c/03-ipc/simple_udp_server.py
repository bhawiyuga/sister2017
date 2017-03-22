import socket

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding socket server ke alamat IP dan Port tertentu
s.bind(('', 9990))

while True :
	# Menerima data dan nama pengirim 
	data, sender = s.recvfrom(100)
	print "Menerima data "+data+" dari client"
	# Tambahkan string OK di depan data yang diterima
	data = "OK "+data
	# Kirim balik ke client
	s.sendto(data, sender)