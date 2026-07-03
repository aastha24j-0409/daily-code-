# Day 25 - PySpark when() and otherwise()

from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("when() and otherwise()") \
    .getOrCreate()

# -------------------------------------
# Sample Data
# -------------------------------------

data = [
    ("John", 25),
    ("Sarah", 30),
    ("Mike", 22),
    ("Emma", 35),
    ("David", 18)
]

df = spark.createDataFrame(
    data,
    ["Name", "Age"]
)

print("Original Data")
df.show()

# -------------------------------------
# Add Age Category
# -------------------------------------

df = df.withColumn(
    "Age_Category",
    when(col("Age") < 18, "Minor")
    .when(col("Age") < 30, "Young Adult")
    .otherwise("Adult")
)

print("Age Categories")
df.show()

# -------------------------------------
# Add Eligibility Column
# -------------------------------------

df = df.withColumn(
    "Eligible_to_Vote",
    when(col("Age") >= 18, "Yes")
    .otherwise("No")
)

print("Voting Eligibility")
df.show()

# -------------------------------------
# Stop Spark
# -------------------------------------

spark.stop()
