# Day 24 - PySpark User Defined Functions (UDF)

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# -------------------------------------
# Create Spark Session
# -------------------------------------

spark = SparkSession.builder \
    .appName("PySpark UDF Practice") \
    .getOrCreate()

# -------------------------------------
# Sample Data
# -------------------------------------

data = [
    ("John", 25),
    ("Sarah", 30),
    ("Mike", 28),
    ("Emma", 35)
]

df = spark.createDataFrame(
    data,
    ["Name", "Age"]
)

print("Original Data")
df.show()

# -------------------------------------
# Create Python Function
# -------------------------------------

def age_group(age):
    if age < 30:
        return "Young"
    else:
        return "Adult"

# -------------------------------------
# Register UDF
# -------------------------------------

age_group_udf = udf(age_group, StringType())

# -------------------------------------
# Apply UDF
# -------------------------------------

df = df.withColumn(
    "Age_Group",
    age_group_udf(df.Age)
)

print("Data with Age Group")
df.show()

# -------------------------------------
# Stop Spark Session
# -------------------------------------

spark.stop()
