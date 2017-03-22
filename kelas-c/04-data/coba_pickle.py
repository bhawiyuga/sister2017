import pickle
from kelas import Mahasiswa

mahasiswaSatu = Mahasiswa("Andi", "12345")
mahasiswaDua = Mahasiswa("Joko", "7890")

# Print parameter objek nya
print mahasiswaSatu.nama+" "+mahasiswaSatu.nim


# Marshal dengan pickle
mahasiswa_pickle = pickle.dumps(mahasiswaSatu)

print mahasiswa_pickle