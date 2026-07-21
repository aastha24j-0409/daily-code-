from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

# Create Spark Session
spark = SparkSession.builder \
    .appName("PySpark UDF Practice") \
    .getOrCreate()

# Sample employee data
data = [
    ("Alice", 65000),
    ("Bob", 85000),
    ("Charlie", 45000),
    ("David", 95000),
    ("Eva", 72000)
]

columns = ["employee", "salary"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

# Custom Python function
def salary_category(salary):
    if salary >= 80000:
        return "High"
    elif salary >= 60000:
        return "Medium"
    else:
        return "Low"

# Convert Python function into PySpark UDF
salary_udf = udf(salary_category, StringType())

# Apply UDF to create a new column
result_df = df.withColumn(
    "salary_category",
    salary_udf(col("salary"))
)

print("Data After Applying UDF")
result_df.show()

spark.stop()
