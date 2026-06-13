# Day 12 - HDFS Architecture

## What is HDFS?

HDFS (Hadoop Distributed File System) is the storage layer of Hadoop.

It is designed to store very large files across multiple machines while providing fault tolerance and high availability.

---

## HDFS Components

### 1. NameNode

The NameNode is the master node.

Responsibilities:
- Maintains metadata
- Tracks file locations
- Manages DataNodes
- Handles client requests

Example:

If a file is stored in Block A, Block B, and Block C, the NameNode knows where each block is located.

---

### 2. DataNode

The DataNode stores actual data blocks.

Responsibilities:
- Store file blocks
- Send heartbeats to NameNode
- Replicate blocks when required

---

## HDFS Working

Step 1:
A file is uploaded to HDFS.

Step 2:
The file is split into blocks.

Example:

```text
Large File
│
├── Block 1
├── Block 2
└── Block 3
```

Step 3:
Blocks are distributed across multiple DataNodes.

```text
NameNode
   │
   ├── DataNode 1 → Block 1
   ├── DataNode 2 → Block 2
   └── DataNode 3 → Block 3
```

---

## Replication

HDFS creates multiple copies of each block.

Example:

```text
Block 1
├── DataNode 1
├── DataNode 2
└── DataNode 3
```

Default replication factor:

```text
3
```

Benefit:

If one machine fails, data is still available.

---

## Advantages of HDFS

- Fault Tolerance
- Scalability
- Distributed Storage
- High Throughput
- Cost Effective

---

## Common HDFS Commands

### List Files

```bash
hdfs dfs -ls /
```

### Create Directory

```bash
hdfs dfs -mkdir /data
```

### Upload File

```bash
hdfs dfs -put sample.csv /data
```

### Display File

```bash
hdfs dfs -cat /data/sample.csv
```

### Delete File

```bash
hdfs dfs -rm /data/sample.csv
```

---

## Interview Questions

### Q1. What is HDFS?

Answer:

HDFS is Hadoop's distributed file system used to store large datasets across multiple machines.

---

### Q2. What is the role of the NameNode?

Answer:

The NameNode manages metadata and tracks where data blocks are stored.

---

### Q3. What is the role of a DataNode?

Answer:

A DataNode stores actual file blocks and communicates with the NameNode.

---

### Q4. What is replication in HDFS?

Answer:

Replication is the process of storing multiple copies of a data block on different DataNodes to ensure fault tolerance.

---

## Quick Revision

NameNode = Metadata

DataNode = Data Storage

Replication = Fault Tolerance

HDFS = Distributed Storage

---

## What I Learned Today

- HDFS is the storage component of Hadoop.
- NameNode manages metadata.
- DataNodes store data blocks.
- Replication protects against data loss.
- HDFS enables distributed storage of big data.
