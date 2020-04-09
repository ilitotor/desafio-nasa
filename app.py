from datetime import datetime
from pyspark import SparkContext
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession
import pyspark.sql.functions as func

sc = SparkContext()
spark = SparkSession(sc)

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

df_jul= spark.read.option("delimiter", " ").csv("NASA_access_log_Jul95")
df_ago = spark.read.option("delimiter", " ").csv("NASA_access_log_Aug95")
df = df_jul.union(df_ago)

print("1. Numero de hosts unico")
total = df.groupby(df._c0).agg(func.countDistinct(df._c0)).count()
print(total, "\n")

print("2. O total de errors 404.")
df.filter("_c6 == 404").groupBy().count().show()

print("3. Os 5 URLs que mais causaram erro 404.")
df.filter(df._c6 == 404).groupBy(df._c5).count().sort('count', ascending=False).limit(5).show()

print("4. Quantidade de erros 404 por dia.")
df = df.withColumn("dias", func.regexp_extract(df._c3, r"\d{2}/\w{3}/\d{4}", 0))
total_dias = df.groupby("dias").agg(func.countDistinct("dias")).count()
total_erros404 = df.select("_c6").filter("_c6 == 404").count()
print(round((total_erros404/total_dias),2), "\n")

print("5. O total de bytes retornados.")
df.withColumn("Bytes", df._c7.cast(IntegerType())).groupBy().sum("Bytes").show()

