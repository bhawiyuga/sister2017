from pyspark import SparkContext

# Buat spark context
sc = SparkContext.getOrCreate()

# Load dari text file
rdd = sc.textFile("file:///vagrant/dataset/tempDataset.txt")
# Ubah dari string ke integer
rddInt = rdd.map(lambda x : int(x))
# Cari nilai max
max_val = rddInt.max()
# Cari nilai average
avg_val = rddInt.mean()

# Cetak hasilnya
# print "Hasilnya adalah "+str(max_val)+" "+str(avg_val)
rddHasil = sc.parallelize([max_val, avg_val])
# Tulis ke file
rddHasil.saveAsTextFile("file:///vagrant/dataset/outAvgMax")