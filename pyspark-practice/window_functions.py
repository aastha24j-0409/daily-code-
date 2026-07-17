from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, col

# Create Spark Session
spark = SparkSession.builder.appName("Window Functions").getOrCreate()

# Sample Employee Data
data = [
    ("Alice", "HR", 65000),
    ("Bob", "IT", 85000),
    ("Charlie", "IT", 85000),
    ("David", "IT", 92000),
    ("Eva", "HR", 72000),
    ("Frank", "Finance", 78000)
]

columns = ["employee", "department", "salary"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

# Window specification
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())

# Add rankings
result = df.withColumn("row_number", row_number().over(window_spec)) \
           .withColumn("rank", rank().over(window_spec)) \
           .withColumn("dense_rank", dense_rank().over(window_spec))

print("Ranking Employees Within Each Department")
result.show()

spark.stop()
