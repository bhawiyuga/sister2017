import socket

# Inisiasi socket baru
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ajukan permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 6666) )

# Kirim data ke server
sock.send("Hello")

# Terima data dari server
data = sock.recv(100)
print data