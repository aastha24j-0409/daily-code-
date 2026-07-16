from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("PySpark Joins").getOrCreate()

# Employee Data
employees = [
    (1, "Alice", 101),
    (2, "Bob", 102),
    (3, "Charlie", 103),
    (4, "David", 104)
]

employee_columns = ["emp_id", "employee_name", "dept_id"]

employee_df = spark.createDataFrame(employees, employee_columns)

# Department Data
departments = [
    (101, "HR"),
    (102, "IT"),
    (103, "Finance"),
    (105, "Marketing")
]

department_columns = ["dept_id", "department"]

department_df = spark.createDataFrame(departments, department_columns)

print("Employees")
employee_df.show()

print("Departments")
department_df.show()

print("Inner Join")
employee_df.join(department_df, "dept_id", "inner").show()

print("Left Join")
employee_df.join(department_df, "dept_id", "left").show()

print("Right Join")
employee_df.join(department_df, "dept_id", "right").show()

print("Full Outer Join")
employee_df.join(department_df, "dept_id", "outer").show()

spark.stop()
