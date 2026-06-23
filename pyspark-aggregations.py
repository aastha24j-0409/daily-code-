# Day 19 - PySpark Aggregations and GroupBy

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, max, min, sum

# Create Spark Session
spark = SparkSession.builder \
    .appName("Aggregations Practice") \
    .getOrCreate()

# Sample Data
data = [
    ("John", "IT", 60000),
    ("Sarah", "HR", 70000),
    ("Mike", "IT", 65000),
    ("Emma", "Finance", 80000),
    ("David", "IT", 55000),
    ("Lisa", "HR", 75000)
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["Name", "Department", "Salary"]
)

print("Original Data")
df.show()

# Count Employees in Each Department
print("Employee Count by Department")
df.groupBy("Department").count().show()

# Average Salary by Department
print("Average Salary by Department")
df.groupBy("Department") \
  .agg(avg("Salary").alias("Average Salary")) \
  .show()

# Maximum Salary by Department
print("Maximum Salary by Department")
df.groupBy("Department") \
  .agg(max("Salary").alias("Max Salary")) \
  .show()

# Minimum Salary by Department
print("Minimum Salary by Department")
df.groupBy("Department") \
  .agg(min("Salary").alias("Min Salary")) \
  .show()

# Total Salary by Department
print("Total Salary by Department")
df.groupBy("Department") \
  .agg(sum("Salary").alias("Total Salary")) \
  .show()

# Stop Spark Session
spark.stop()
