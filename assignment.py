from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from pyspark.sql.functions import col, array_contains, avg, max, count

# ==========================================================
# Q1
# Read Department.txt, create doubleSalary column,
# write output as department.parquet
# ==========================================================

def q1(spark):

    schema = StructType([
        StructField("dept_name", StringType(), True),
        StructField("dept_id", IntegerType(), True),
        StructField("salary", LongType(), True)
    ])

    df = spark.read \
        .option("header", "false") \
        .schema(schema) \
        .csv("/data/test/text/department.txt")

    result = df.withColumn(
        "doubleSalary",
        col("salary") * 2
    )

    result.select(
        "dept_name",
        "salary",
        "doubleSalary"
    ).write \
        .mode("overwrite") \
        .parquet("/data/test/text/department.parquet")


# ==========================================================
# Q2
# Read student.json
# Return firstname and gender of students
# learning Java and not from OH
# ==========================================================

def q2(spark):

    df = spark.read.json("file:///home/takeo/student.json")

    result = df.filter(
        array_contains(col("languages"), "Java") &
        (col("state") != "OH")
    ).select(
        col("name.firstname").alias("firstname"),
        col("gender")
    )

    result.show()


# ==========================================================
# Q3
# Read employee.json
# Remove duplicates
# Write ORC partitioned by department
# Return departments by mean salary descending
# ==========================================================

def q3(spark):

    df = spark.read.json("file:///home/takeo/employee.json")

    distinct_df = df.dropDuplicates()

    distinct_df.write \
        .mode("overwrite") \
        .partitionBy("department") \
        .orc("/data/test/text/employee.orc")

    result = distinct_df.groupBy("department") \
        .agg(
            avg("salary").alias("meanSalary")
        ) \
        .orderBy(col("meanSalary").desc())

    result.show()


# ==========================================================
# Q4
# Join employee and department
# Find max salary and employee count
# Store in Hive partitioned table
# ==========================================================

def q4(spark):

    emp_df = spark.read.json("file:///home/takeo/employee.json")

    dept_df = spark.read.json("file:///home/takeo/department.json")

    joined = emp_df.join(
        dept_df,
        emp_df.emp_dept_id == dept_df.dept_id,
        "inner"
    )

    result = joined.groupBy("dept_name") \
        .agg(
            max("salary").alias("maxSalary"),
            count("emp_id").alias("employeesCount")
        )

    spark.sql("DROP TABLE IF EXISTS default.part_department")

    spark.sql("""
        CREATE TABLE default.part_department
        (
            maxSalary LONG,
            employeesCount LONG
        )
        PARTITIONED BY (dept_name STRING)
        STORED AS PARQUET
    """)

    spark.conf.set("hive.exec.dynamic.partition", "true")
    spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

    result.select(
        "maxSalary",
        "employeesCount",
        "dept_name"
    ).write \
        .mode("overwrite") \
        .insertInto("default.part_department")

    spark.sql("SELECT * FROM default.part_department").show()


# ==========================================================
# Q5
# Read CSV
# Generate 50% sample
# Create Hive partitioned table
# Max 3 records/file
# Run Hive SQL
# ==========================================================

def q5(spark):

    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("file:///home/takeo/simple-zipcodes.csv")

    sample_df = df.sample(
        fraction=0.5,
        seed=42
    )

    print("Sample Count :", sample_df.count())

    spark.sql("DROP TABLE IF EXISTS default.zipcode_partitioned")

    spark.sql("""
        CREATE TABLE default.zipcode_partitioned
        (
            RecordNumber INT,
            Country STRING,
            Zipcode INT
        )
        PARTITIONED BY
        (
            State STRING,
            City STRING
        )
        STORED AS PARQUET
    """)

    spark.conf.set("hive.exec.dynamic.partition", "true")
    spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
    spark.conf.set("spark.sql.files.maxRecordsPerFile", "3")

    sample_df.select(
        "RecordNumber",
        "Country",
        "Zipcode",
        "State",
        "City"
    ).write \
        .mode("overwrite") \
        .insertInto("default.zipcode_partitioned")

    spark.sql("""
        SELECT *
        FROM default.zipcode_partitioned
        WHERE State != 'AL'
        AND City != 'SPRINGVILLE'
    """).show()


# ==========================================================
# Main Program
# ==========================================================

if __name__ == "__main__":

    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("PySpark Assessment") \
        .getOrCreate()

    q1(spark)
    q2(spark)
    q3(spark)

    spark_hive = SparkSession.builder \
        .master("local[1]") \
        .appName("PySpark Hive Assessment") \
        .enableHiveSupport() \
        .getOrCreate()

    q4(spark_hive)
    q5(spark_hive)
