from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName('Hello World').getOrCreate()

print("Welcome to Spark Object")

rdd = spark.sparkContext.parallelize([1,2,3])
print(rdd.first())