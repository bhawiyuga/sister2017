import socket

#Inisiasi object socket UDP/ipv4
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Kirim string ke server
sock.sendto("Hello", ('127.0.0.1', 7777) )
# Terima data kembalian dari server
data, address = sock.recvfrom(100)
print data