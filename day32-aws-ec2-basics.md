# Day 32 - Amazon EC2 Basics

## What is Amazon EC2?

Amazon EC2 (Elastic Compute Cloud) is a web service that provides virtual servers in the cloud.

It allows you to launch, manage, and scale virtual machines without buying physical hardware.

---

## Why Use EC2?

Instead of purchasing a physical server, you can create a virtual server in AWS within minutes.

Benefits:

- Scalable
- Secure
- Flexible
- Pay only for what you use

---

## Key Features

- Launch virtual machines
- Choose different operating systems
- Scale resources up or down
- Secure access using Security Groups
- Connect remotely using SSH (Linux) or RDP (Windows)

---

## EC2 Components

### 1. AMI (Amazon Machine Image)

An AMI is a template used to launch an EC2 instance.

Examples:

- Amazon Linux
- Ubuntu
- Windows Server

---

### 2. Instance Type

Determines the CPU, memory, and storage available.

Examples:

- t2.micro
- t3.micro
- m5.large

---

### 3. Key Pair

A Key Pair is used to securely connect to an EC2 instance.

- Public Key
- Private Key (.pem file)

Keep the private key safe because it cannot be downloaded again.

---

### 4. Security Group

A Security Group acts as a virtual firewall.

It controls:

- SSH (Port 22)
- HTTP (Port 80)
- HTTPS (Port 443)

---

## EC2 Launch Process

1. Choose an AMI.
2. Select an Instance Type.
3. Configure storage.
4. Create or select a Key Pair.
5. Configure the Security Group.
6. Launch the instance.

---

## Common Use Cases

- Host websites
- Run applications
- Data processing
- Development and testing
- ETL jobs

---

## Interview Questions

### Q1. What is Amazon EC2?

Answer:

Amazon EC2 is a service that provides virtual servers in the AWS cloud.

---

### Q2. What is an AMI?

Answer:

An Amazon Machine Image (AMI) is a template used to create EC2 instances.

---

### Q3. What is a Security Group?

Answer:

A Security Group is a virtual firewall that controls inbound and outbound traffic to an EC2 instance.

---

### Q4. What is a Key Pair?

Answer:

A Key Pair is used for secure authentication when connecting to an EC2 instance.

---

## Quick Revision

AWS = Cloud Platform

EC2 = Virtual Machine

AMI = Machine Image

Instance Type = CPU and Memory Configuration

Security Group = Firewall

Key Pair = Secure Login

---

## What I Learned Today

- Learned what Amazon EC2 is.
- Understood the purpose of AMIs.
- Learned how instance types define compute resources.
- Understood the role of Security Groups.
- Learned how Key Pairs provide secure access to EC2 instances.
