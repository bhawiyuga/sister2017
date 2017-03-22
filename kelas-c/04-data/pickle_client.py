import socket
import pickle
from kelas import Mahasiswa

# Inisiasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bikin koneksi ke server (3-way handshaking)
s.connect(('127.0.0.1', 8889))

mahasiswaSatu = Mahasiswa("Andi", "1234")

mahasiswa_str = pickle.dumps(mahasiswaSatu)

# Kirim data
s.send(mahasiswa_str)
# Terima balasan dari server
data = s.recv(100000)
# Cetak balasan dari server
print data
# Tutup koneksi
s.close()