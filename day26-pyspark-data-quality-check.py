# Day 26 - PySpark Data Quality Checker

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("Data Quality Check") \
    .getOrCreate()

# -------------------------------------
# Sample Data
# -------------------------------------

data = [
    (1, "John", 25, "IT"),
    (2, "Sarah", None, "HR"),
    (3, "Mike", 28, None),
    (4, "Emma", 35, "Finance"),
    (5, "David", None, "IT"),
    (6, None, 30, "HR")
]

df = spark.createDataFrame(
    data,
    ["ID", "Name", "Age", "Department"]
)

print("Original Data")
df.show()

# -------------------------------------
# Check Total Rows
# -------------------------------------

print("Total Rows:")
print(df.count())

# -------------------------------------
# Check for Null Values
# -------------------------------------

print("Null Values in Each Column")

df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
]).show()

# -------------------------------------
# Check Duplicate IDs
# -------------------------------------

print("Duplicate IDs")

df.groupBy("ID") \
  .count() \
  .filter(col("count") > 1) \
  .show()

# -------------------------------------
# Remove Rows with Null Name
# -------------------------------------

print("Remove Rows with Missing Name")

clean_df = df.dropna(subset=["Name"])

clean_df.show()

# -------------------------------------
# Display Final Row Count
# -------------------------------------

print("Rows After Cleaning:")
print(clean_df.count())

# -------------------------------------
# Stop Spark
# -------------------------------------

spark.stop()
