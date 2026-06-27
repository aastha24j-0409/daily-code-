# Day 23 - PySpark Window Functions

from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number, rank, dense_rank
from pyspark.sql.window import Window

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("Window Functions") \
    .getOrCreate()

# -------------------------------------
# Sample Data
# -------------------------------------

data = [
    ("John", "IT", 60000),
    ("Sarah", "HR", 70000),
    ("Mike", "IT", 65000),
    ("Emma", "Finance", 80000),
    ("David", "IT", 55000),
    ("Lisa", "HR", 70000)
]

df = spark.createDataFrame(
    data,
    ["Name", "Department", "Salary"]
)

print("Original Data")
df.show()

# -------------------------------------
# Create Window Specification
# -------------------------------------

windowSpec = Window.partitionBy("Department").orderBy(df.Salary.desc())

# -------------------------------------
# row_number()
# -------------------------------------

print("Row Number")

df.withColumn(
    "Row_Number",
    row_number().over(windowSpec)
).show()

# -------------------------------------
# rank()
# -------------------------------------

print("Rank")

df.withColumn(
    "Rank",
    rank().over(windowSpec)
).show()

# -------------------------------------
# dense_rank()
# -------------------------------------

print("Dense Rank")

df.withColumn(
    "Dense_Rank",
    dense_rank().over(windowSpec)
).show()

spark.stop()
