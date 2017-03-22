import socket

#Inisialisasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim string ke server
s.sendto("Selamat sore", ('127.0.0.1',9990) )
# Baca balasan dari server
data, sender = s.recvfrom(100)
# Cetak balasannya
print data