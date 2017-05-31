from pyspark import SparkContext

sc = SparkContext.getOrCreate()

# Load dataset
rdd = sc.textFile("file:///vagrant/dataset/tempDataset.txt")

# Cari nilai maximum
suhuMax = rdd.map(lambda x: int(x)).max()
suhuAvg = rdd.map(lambda x: int(x)).mean()

rddHasil = sc.parallelize([suhuMax, suhuAvg])

rddHasil.saveAsTextFile("file:///vagrant/dataset/hasilakhir")

#print "Hasilnya adalah : "+str(data)