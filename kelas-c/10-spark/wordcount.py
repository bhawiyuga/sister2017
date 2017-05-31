from pyspark import SparkContext

sc = SparkContext.getOrCreate()

# Load dataset
rdd = sc.textFile("file:///vagrant/dataset/ibubudi.txt")

# Split text
rddSplit = rdd.flatMap(lambda line: line.split(" ") )
rddSplit.saveAsTextFile("file:///vagrant/dataset/hasil1")

# Beri value 1 untuk semua word
rddValue = rddSplit.map(lambda word: (word, 1) )
rddValue.saveAsTextFile("file:///vagrant/dataset/hasil2")

# Kelompokkan data dengan key yang sama
# Jumlahkan value-nya
rddAkhir = rddValue.reduceByKey( lambda x,y : x+y )
rddAkhir.saveAsTextFile("file:///vagrant/dataset/hasil3")

