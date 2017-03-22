import socket
import pickle
from mahasiswa import Mahasiswa

# Inisiasi socket baru
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ajukan permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 6666) )

mahasiswa_satu = Mahasiswa("Andi", "1234")

mahasiswa_pickle = pickle.dumps(mahasiswa_satu)

# Kirim data ke server
sock.send(mahasiswa_pickle)

# Terima data dari server
data = sock.recv(1024)
print data