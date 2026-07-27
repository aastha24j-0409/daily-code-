from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Sample sales data
data = [
    (1, "Laptop", 1200.0, 2),
    (2, "Phone", None, 1),
    (3, "Tablet", 600.0, 0),
    (4, None, 450.0, 3),
    (5, "Monitor", -200.0, 1),
    (6, "Keyboard", 80.0, 5)
]

columns = ["product_id", "product_name", "price", "quantity"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

# -------------------------
# Data Quality Checks
# -------------------------

# Null values
print("Rows with Null Values")
df.filter(
    col("product_name").isNull() |
    col("price").isNull()
).show()

# Invalid prices
print("Rows with Invalid Price")
df.filter(col("price") <= 0).show()

# Invalid quantity
print("Rows with Invalid Quantity")
df.filter(col("quantity") <= 0).show()

# Valid records
valid_df = df.filter(
    col("product_name").isNotNull() &
    col("price").isNotNull() &
    (col("price") > 0) &
    (col("quantity") > 0)
)

print("Valid Records")
valid_df.show()

spark.stop()
