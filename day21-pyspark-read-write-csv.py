# Day 21 - Reading and Writing CSV Files in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("Read and Write CSV") \
    .getOrCreate()

# -------------------------------
# Read CSV File
# -------------------------------

df = spark.read.csv(
    "employees.csv",
    header=True,
    inferSchema=True
)

print("Original Data")
df.show()

# -------------------------------
# Display Schema
# -------------------------------

print("Schema")
df.printSchema()

# -------------------------------
# Select Columns
# -------------------------------

print("Employee Names")

df.select("Name", "Department").show()

# -------------------------------
# Filter Employees
# -------------------------------

print("Employees with Salary > 60000")

df.filter(col("Salary") > 60000).show()

# -------------------------------
# Group By Department
# -------------------------------

print("Employees Per Department")

df.groupBy("Department").count().show()

# -------------------------------
# Write Data to CSV
# -------------------------------

df.write.mode("overwrite").csv(
    "output/employees_output",
    header=True
)

print("CSV written successfully!")

spark.stop()
