from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, count

# Create Spark Session
spark = SparkSession.builder.appName("GroupBy Aggregations").getOrCreate()

# Sample Sales Data
data = [
    (1, "Laptop", "Electronics", 1200),
    (2, "Phone", "Electronics", 800),
    (3, "Chair", "Furniture", 150),
    (4, "Table", "Furniture", 300),
    (5, "Laptop", "Electronics", 1300),
    (6, "Chair", "Furniture", 180)
]

columns = ["id", "product", "category", "sales"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

print("Total Sales by Category")
df.groupBy("category").agg(
    sum("sales").alias("total_sales")
).show()

print("Average Sales by Category")
df.groupBy("category").agg(
    avg("sales").alias("average_sales")
).show()

print("Sales Statistics")
df.groupBy("category").agg(
    count("*").alias("transactions"),
    max("sales").alias("highest_sale"),
    min("sales").alias("lowest_sale")
).show()

spark.stop()
