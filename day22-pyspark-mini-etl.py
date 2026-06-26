# Day 22 - Mini ETL Pipeline in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, avg

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("Mini ETL Pipeline") \
    .getOrCreate()

# -------------------------------------
# Sample Employee Data
# -------------------------------------

data = [
    ("John", "IT", 60000),
    ("Sarah", "HR", 70000),
    ("Mike", "IT", 65000),
    ("Emma", "Finance", 80000),
    ("David", None, 55000),
    ("Lisa", "HR", None)
]

df = spark.createDataFrame(
    data,
    ["Name", "Department", "Salary"]
)

print("Original Data")
df.show()

# -------------------------------------
# Extract
# -------------------------------------

print("Step 1: Extract")
df.show()

# -------------------------------------
# Transform
# -------------------------------------

print("Step 2: Transform")

# Remove rows with missing values
df_clean = df.dropna()

# Convert department names to uppercase
df_clean = df_clean.withColumn(
    "Department",
    upper(col("Department"))
)

# Filter employees earning more than 60000
df_filtered = df_clean.filter(col("Salary") > 60000)

df_filtered.show()

# -------------------------------------
# Aggregate
# -------------------------------------

print("Step 3: Aggregate")

df_filtered.groupBy("Department") \
    .agg(avg("Salary").alias("Average Salary")) \
    .show()

# -------------------------------------
# Load
# -------------------------------------

print("Step 4: Load")

df_filtered.write \
    .mode("overwrite") \
    .csv("output/clean_employee_data", header=True)

print("Pipeline completed successfully!")

# -------------------------------------
# Stop Spark
# -------------------------------------

spark.stop()
