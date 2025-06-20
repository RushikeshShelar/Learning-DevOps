# ☁️ Cloud Computing & AWS Overview

## 🌐 What is Cloud Computing?

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access services such as compute power, storage, and databases from a cloud provider.

### 🔑 Key Characteristics
- **On-demand self-service** – provision resources without human interaction.
- **Broad network access** – available over the internet or intranet.
- **Resource pooling** – shared resources serving multiple users.
- **Rapid elasticity** – scale resources up or down as needed.
- **Measured service** – pay only for what you use.

---

## 🏗️ Types of Cloud Deployment Models

| Deployment Model | Description |
|------------------|-------------|
| **Public Cloud** | Resources are owned and operated by third-party cloud service providers (e.g., AWS, Azure, GCP) and delivered over the internet. |
| **Private Cloud** | Cloud infrastructure is exclusively used by a single organization. Can be on-premises or hosted by a third-party. |
| **Hybrid Cloud** | Combines public and private clouds, allowing data and applications to move between them. |

---

## 📦 Cloud Service Models

| Service Model | Description | Example Services |
|---------------|-------------|------------------|
| **IaaS (Infrastructure as a Service)** | Provides virtualized computing resources over the internet. | EC2, S3 (AWS), Compute Engine (GCP) |
| **PaaS (Platform as a Service)** | Provides tools and environments to build, test, and deploy applications. | AWS Elastic Beanstalk, Heroku |
| **SaaS (Software as a Service)** | Delivers software applications over the internet, usually via a browser. | Gmail, Microsoft 365, Dropbox |

---

## ☁️ Major Cloud Providers

| Provider | Description |
|----------|-------------|
| **AWS (Amazon Web Services)** | Market leader in cloud services. Offers 200+ services globally. |
| **Microsoft Azure** | Strong enterprise support. Deep integration with Microsoft tools. |
| **Google Cloud Platform (GCP)** | Known for data analytics, machine learning, and Kubernetes. |
| **IBM Cloud** | Offers hybrid cloud solutions and enterprise-grade services. |
| **Oracle Cloud** | Focuses on database and business apps in the cloud. |

---

## 🟡 What is AWS?

**Amazon Web Services (AWS)** is a secure cloud services platform by Amazon that offers compute power, database storage, content delivery, and other functionalities to help businesses scale and grow.

### ✅ Key Benefits
- **Global Reach** – Data centers in multiple regions and availability zones.
- **Scalability** – Easily scale up/down based on workload.
- **Pay-as-you-go** – Cost-effective and flexible pricing.
- **Secure** – Built-in compliance, encryption, and access control tools.

---

## 🌍 AWS Global Infrastructure

- **Regions** – Geographical areas hosting multiple data centers (e.g., `us-east-1`, `ap-south-1`).
- **Availability Zones (AZs)** – Isolated data centers within a region.
- **Edge Locations** – Used by services like CloudFront for content delivery (CDN).

---

## 🔧 Common AWS Services Categories

| Category         | Service Examples                  |
|------------------|-----------------------------------|
| **Compute**      | EC2, Lambda, Elastic Beanstalk    |
| **Storage**      | S3, EBS, Glacier                  |
| **Database**     | RDS, DynamoDB, Aurora             |
| **Networking**   | VPC, Route 53, CloudFront         |
| **Security**     | IAM, KMS, Shield                  |
| **Monitoring**   | CloudWatch, CloudTrail            |
| **DevOps Tools** | CodePipeline, CodeBuild, CodeDeploy |

---

## 📌 Real-World Scenario

Imagine you're building a scalable web app:

- You deploy your app using **EC2** (compute).
- Store static assets in **S3** (storage).
- Use **RDS** for relational database needs.
- Secure it using **IAM** roles and policies.
- Monitor performance using **CloudWatch**.
- Distribute content globally with **CloudFront**.

All without touching a single physical server — this is the power of cloud computing.
