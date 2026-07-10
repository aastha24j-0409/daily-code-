# Day 31 - Amazon S3 Basics

## What is Amazon S3?

Amazon S3 (Simple Storage Service) is an object storage service provided by AWS.

It is used to store and retrieve any amount of data from anywhere in the world.

S3 is one of the most widely used AWS services in data engineering, analytics, backups, and machine learning.

---

## Features of Amazon S3

- Highly Durable (99.999999999%)
- Scalable
- Secure
- Pay-as-you-go
- Accessible from anywhere

---

## Common Use Cases

- Store CSV files
- Store images and videos
- Data lake storage
- Application backups
- Log file storage
- Machine learning datasets

---

## S3 Terminology

### Bucket

A bucket is a container that stores objects.

Example:

Bucket Name:

employee-data

---

### Object

An object is a file stored inside a bucket.

Example:

employees.csv

sales.parquet

customer.json

---

### Key

The unique path or name of an object inside a bucket.

Example:

data/2026/employees.csv

---

## S3 Storage Classes

### S3 Standard

- Frequently accessed data
- High availability
- Low latency

---

### S3 Standard-IA

- Infrequently accessed data
- Lower storage cost
- Retrieval fee applies

---

### S3 Glacier

- Long-term archival
- Very low storage cost
- Retrieval can take minutes or hours

---

## Benefits of S3

- Unlimited storage
- High durability
- Automatic scaling
- Secure with IAM
- Versioning support

---

## Example Data Engineering Workflow

CSV Files
        ↓
Amazon S3
        ↓
AWS Glue / PySpark
        ↓
Amazon Redshift
        ↓
Power BI / Tableau

---

## Interview Questions

### Q1. What is Amazon S3?

Answer:

Amazon S3 is an object storage service that stores and retrieves files of any size over the internet.

---

### Q2. What is a bucket?

Answer:

A bucket is a container used to store objects in Amazon S3.

---

### Q3. What is an object?

Answer:

An object is a file stored inside an S3 bucket.

---

### Q4. Why is Amazon S3 important for data engineers?

Answer:

Because it is commonly used as a data lake to store raw, processed, and analytics-ready data for ETL pipelines.

---

## Quick Revision

AWS = Cloud Platform

S3 = Object Storage

Bucket = Container

Object = File

Key = File Path

---

## What I Learned Today

- Learned what Amazon S3 is.
- Understood buckets, objects, and keys.
- Explored common S3 storage classes.
- Learned how S3 fits into a data engineering pipeline.
- Understood why S3 is widely used for data lakes.
