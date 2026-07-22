from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, round

# Create Spark Session
spark = SparkSession.builder \
    .appName("Mini ETL Pipeline") \
    .getOrCreate()

# -------------------------
# 1. EXTRACT
# -------------------------

data = [
    (1, "alice", "electronics", 1200.00, 2),
    (2, "bob", "furniture", 450.00, 1),
    (3, "charlie", "electronics", None, 3),
    (4, "david", "clothing", 150.00, 4),
    (5, "eva", "electronics", 800.00, 2)
]

columns = [
    "customer_id",
    "customer_name",
    "category",
    "price",
    "quantity"
]

df = spark.createDataFrame(data, columns)

print("Raw Data")
df.show()

# -------------------------
# 2. TRANSFORM
# -------------------------

# Remove records with missing prices
clean_df = df.dropna(subset=["price"])

# Standardize text
clean_df = clean_df.withColumn(
    "customer_name",
    upper(col("customer_name"))
)

clean_df = clean_df.withColumn(
    "category",
    upper(col("category"))
)

# Calculate total sale
clean_df = clean_df.withColumn(
    "total_sale",
    round(col("price") * col("quantity"), 2)
)

# Keep required columns
final_df = clean_df.select(
    "customer_id",
    "customer_name",
    "category",
    "price",
    "quantity",
    "total_sale"
)

print("Transformed Data")
final_df.show()

# -------------------------
# 3. LOAD
# -------------------------

final_df.write \
    .mode("overwrite") \
    .parquet("output/clean_sales")

print("ETL Pipeline Completed Successfully")

spark.stop()
