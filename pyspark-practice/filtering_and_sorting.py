from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder.appName("Filtering and Sorting").getOrCreate()

# Sample Employee Data
data = [
    (1, "Alice", "HR", 65000),
    (2, "Bob", "IT", 85000),
    (3, "Charlie", "Finance", 72000),
    (4, "David", "IT", 90000),
    (5, "Eva", "HR", 58000)
]

columns = ["id", "name", "department", "salary"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

print("Employees with salary greater than 70000")
df.filter(col("salary") > 70000).show()

print("Employees from IT Department")
df.filter(col("department") == "IT").show()

print("Sort by Salary (Highest First)")
df.orderBy(col("salary").desc()).show()

spark.stop()
