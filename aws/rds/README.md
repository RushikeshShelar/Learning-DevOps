# 🛢️ AWS RDS (Relational Database Service)

## 📚 What are Databases?

A **database** is a structured collection of data stored electronically for easy access, management, and retrieval.

- **SQL (Relational Databases)**:
  - Structured schema (tables, rows, columns).
  - Examples: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server.
- **NoSQL (Non-relational Databases)**:
  - Flexible schema (JSON, key-value, graphs, etc.).
  - Examples: MongoDB, DynamoDB, Cassandra.

---

## 🖥️ Hosting a Database on EC2

You can install and manage any DB engine manually by setting it up on an EC2 instance.

### ✅ When to Use:
- Custom configurations or legacy systems.
- Full control over OS, DB engine, and environment.

### ❌ Limitations:
- You handle everything: setup, backups, scaling, high availability.
- Not recommended for production workloads unless necessary.

---

## 🔧 EC2 Database Setup (MariaDB Demo)

```bash
# Login as root
sudo su -

# Install MariaDB
yum -y install mariadb-server wget
systemctl enable mariadb
systemctl start mariadb
yum -y update

# Set Environment Variables
DBName=ec2db
DBPassword=admin123456
DBRootPassword=admin123456
DBUser=ec2dbuser

# Create DB, User & Grant Access
echo "CREATE DATABASE ${DBName};" >> /tmp/db.setup
echo "CREATE USER '${DBUser}' IDENTIFIED BY '${DBPassword}';" >> /tmp/db.setup
echo "GRANT ALL PRIVILEGES ON *.* TO '${DBUser}'@'%';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysqladmin -u root password "${DBRootPassword}"
mysql -u root --password="${DBRootPassword}" < /tmp/db.setup
rm /tmp/db.setup

# Add Dummy Data
mysql -u root --password="${DBRootPassword}"
USE ec2db;
CREATE TABLE table1 (id INT, name VARCHAR(45));
INSERT INTO table1 VALUES(1, 'Virat'), (2, 'Sachin'), (3, 'Dhoni'), (4, 'ABD');
SELECT * FROM table1;
```

---

## 🌩️ What is AWS RDS?
RDS (Relational Database Service) is a fully managed service for running SQL databases in the cloud. It handles provisioning, patching, backup, replication, and scaling.

### Benefits:
- Automated backups and patching.
- High availability with Multi-AZ.
- Built-in monitoring and performance insights.
- Easy to scale vertically.
- Secure with VPC, IAM, and encryption.

---

### ✅ RDS Supported Engines
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- Microsoft SQL Server
- Amazon Aurora (AWS-optimized DB engine)

## 🏗️ How to Setup RDS
1. Create Subnet Group
- Choose VPC and select subnets (from different AZs for Multi-AZ setup).
-  This tells AWS where RDS instances can be placed.
2. Create RDS Instance
- Standard/Create DB (avoid Easy Create for full control).
- Choose engine (e.g., MariaDB).
- Set DB identifier, username, and password.
- Instance class (CPU/RAM), storage size, and autoscaling options.
- Enable Multi-AZ deployment for failover support.
- Choose subnet group, VPC, and security group.
- (Optional) Enable backups, monitoring, maintenance windows.
3. Connectivity
- Attach a security group that allows traffic on port 3306 from EC2/private IP range.
- Public access: No (prefer internal access).
- Ensure EC2 and RDS are in the same VPC/Subnet for communication.

---

## 🔄 Migrating Data from EC2 to RDS
After RDS is ready, you can migrate the existing DB from EC2 using mysqldump.

```bash
# Dump EC2 Database
mysqldump -u root -p ec2db > ec2db.sql

# Restore into RDS (change RDS endpoint, username, and db name)
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p rdsdb < ec2db.sql

# Verify on RDS
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p
USE rdsdb;
SELECT * FROM table1;
```
> ⚠️ Ensure your EC2 security group allows outbound access and RDS security group allows inbound access on port 3306.

---

## 🛡️ Security Best Practices
- Use IAM authentication (optional) to manage DB credentials via AWS IAM.
- Enable encryption at rest and in-transit.
- Configure automatic backups and snapshots.
- Use parameter groups for tuning DB engine settings.
- 🧠 Extra Concepts to Explore (Optional)
- Read Replicas: For scaling read-heavy applications.
- Performance Insights: Monitor slow queries and CPU usage.
- Event Subscriptions: Get alerts for failures or instance events.
- Database Cloning: Create new DBs from existing ones for testing.
- CloudWatch Alarms: Trigger alarms when RDS CPU/storage crosses threshold.