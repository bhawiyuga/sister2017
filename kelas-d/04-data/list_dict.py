import json

list_hari = ["Senin", "Selasa", "Rabu", "Kamis"]
#print list_hari[1]

dict_ibukota = { "Indonesia" : "Jakarta", "Malaysia":"Kuala Lumpur", "India" : "New Delhi"}
#print dict_ibukota["Indonesia"]

list_mahasiswa = [
	{"nama" : "Andi", "nim":"1234", "jurusan":"TiF"},
	{"nama" : "Joko", "nim":"7890", "jurusan":"TekKom"}
]

#print list_mahasiswa[0]["nama"]+" "+list_mahasiswa[0]["nim"]

# Marshalling
list_mahasiswa_json = json.dumps(list_mahasiswa)

# Unmarshalling
list_mahasiswa_unmarshal = json.loads(list_mahasiswa_json)
print list_mahasiswa_unmarshal[0]["nama"]