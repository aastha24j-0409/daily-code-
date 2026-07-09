# Day 28 - Employee Performance Analysis

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, when

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("Employee Performance Analysis") \
    .getOrCreate()

# -------------------------------------
# Sample Employee Data
# -------------------------------------

data = [
    (101, "John", "IT", 65000),
    (102, "Sarah", "HR", 72000),
    (103, "Mike", "IT", 58000),
    (104, "Emma", "Finance", 85000),
    (105, "David", "IT", 48000),
    (106, "Lisa", "HR", 69000)
]

columns = ["EmployeeID", "Name", "Department", "Salary"]

df = spark.createDataFrame(data, columns)

print("Employee Data")
df.show()

# -------------------------------------
# Add Performance Category
# -------------------------------------

df = df.withColumn(
    "Performance",
    when(col("Salary") >= 70000, "High Performer")
    .when(col("Salary") >= 55000, "Good Performer")
    .otherwise("Needs Improvement")
)

print("Performance Categories")
df.show()

# -------------------------------------
# Average Salary by Department
# -------------------------------------

print("Average Salary by Department")

df.groupBy("Department") \
  .agg(avg("Salary").alias("Average Salary")) \
  .show()

# -------------------------------------
# Total Salary by Department
# -------------------------------------

print("Total Salary by Department")

df.groupBy("Department") \
  .agg(sum("Salary").alias("Total Salary")) \
  .show()

# -------------------------------------
# High Performers
# -------------------------------------

print("High Performers")

df.filter(col("Performance") == "High Performer") \
  .show()

# -------------------------------------
# Sort by Salary
# -------------------------------------

print("Employees Sorted by Salary")

df.orderBy(col("Salary").desc()).show()

# -------------------------------------
# Stop Spark
# -------------------------------------

spark.stop()
