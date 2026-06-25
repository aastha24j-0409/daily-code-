# Day 20 - PySpark Joins

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("PySpark Joins") \
    .getOrCreate()

# Employee Data
employees = [
    (1, "John", 101),
    (2, "Sarah", 102),
    (3, "Mike", 101),
    (4, "Emma", 103),
    (5, "David", 104)
]

employee_df = spark.createDataFrame(
    employees,
    ["EmployeeID", "Name", "DepartmentID"]
)

# Department Data
departments = [
    (101, "IT"),
    (102, "HR"),
    (103, "Finance")
]

department_df = spark.createDataFrame(
    departments,
    ["DepartmentID", "Department"]
)

print("Employees")
employee_df.show()

print("Departments")
department_df.show()

# -----------------------------
# Inner Join
# -----------------------------
print("Inner Join")

employee_df.join(
    department_df,
    on="DepartmentID",
    how="inner"
).show()

# -----------------------------
# Left Join
# -----------------------------
print("Left Join")

employee_df.join(
    department_df,
    on="DepartmentID",
    how="left"
).show()

# -----------------------------
# Right Join
# -----------------------------
print("Right Join")

employee_df.join(
    department_df,
    on="DepartmentID",
    how="right"
).show()

# -----------------------------
# Full Outer Join
# -----------------------------
print("Full Outer Join")

employee_df.join(
    department_df,
    on="DepartmentID",
    how="outer"
).show()

spark.stop()
