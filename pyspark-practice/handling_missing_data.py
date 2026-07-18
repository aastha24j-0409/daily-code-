from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder.appName("Handling Missing Data").getOrCreate()

# Sample Data with Missing Values
data = [
    (1, "Alice", 25, 65000),
    (2, "Bob", None, 85000),
    (3, None, 30, None),
    (4, "David", 28, 72000),
    (5, "Eva", None, 58000)
]

columns = ["id", "name", "age", "salary"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

# Drop rows with any null values
print("Drop Rows with Null Values")
df.dropna().show()

# Fill null values
print("Fill Missing Values")
filled_df = df.fillna({
    "name": "Unknown",
    "age": 0,
    "salary": 0
})
filled_df.show()

# Filter rows where salary is not null
print("Rows with Non-Null Salary")
df.filter(col("salary").isNotNull()).show()

spark.stop()
