from pyspark import SparkContext

sc = SparkContext.getOrCreate()

rdd = sc.textFile("file:///vagrant/dataset/ibubudi.txt")
# Split by spasi
rddSplit = rdd.flatMap(lambda line : line.split(" "))
# Beri value 1 utk tiap kata
rddValue = rddSplit.map( lambda word: (word,1) )
# Grouping dan reduce by key
rddHasil = rddValue.reduceByKey( lambda x,y : x+y)
# Tulis hasilnya ke file
rddHasil.saveAsTextFile("file:///vagrant/dataset/outIbuBudi")