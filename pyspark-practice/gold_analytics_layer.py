from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    sum,
    avg,
    count,
    round
)

# Create Spark Session
spark = SparkSession.builder \
    .appName("Gold Analytics Layer") \
    .getOrCreate()

# ---------------------------------
# 1. READ CLEANED PARQUET DATA
# ---------------------------------

df = spark.read.parquet(
    "output/clean_sales"
)

print("Cleaned Sales Data")
df.show()

# ---------------------------------
# 2. CREATE GOLD AGGREGATION
# ---------------------------------

gold_df = df.groupBy(
    "category"
).agg(

    round(
        sum("total_sale"), 2
    ).alias("total_revenue"),

    count("*").alias(
        "total_transactions"
    ),

    round(
        avg("total_sale"), 2
    ).alias("average_sale")

)

# ---------------------------------
# 3. SORT BY REVENUE
# ---------------------------------

gold_df = gold_df.orderBy(
    "total_revenue",
    ascending=False
)

print("Gold Analytics Table")
gold_df.show()

# ---------------------------------
# 4. SAVE GOLD DATA
# ---------------------------------

gold_df.write \
    .mode("overwrite") \
    .parquet("output/gold_sales_summary")

print(
    "Gold analytics layer created successfully!"
)

spark.stop()
