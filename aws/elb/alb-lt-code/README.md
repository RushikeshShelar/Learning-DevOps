# 🚀 Node.js + AWS Load Balancer Demo

This project demonstrates how to deploy a basic **Node + Express** app across multiple EC2 instances using an **Application Load Balancer (ALB)** and **Auto Scaling Group (ASG)**.

---

## 🧩 Architecture Overview

- Upload zipped Node.js app to S3
- Create a Launch Template with install + run script
- Auto Scaling Group (ASG) provisions 3 EC2s
- Application Load Balancer (ALB) forwards traffic to the instances
- Each refresh routes to a different EC2 → showing load balancing in action

---

## ⚙️ Setup Steps

### 1️⃣ Upload App to S3

- Create an **S3 bucket**
- Upload your `app.zip` (should contain `server.js` and `package.json`)

Example structure:
```
/app
  ├── server.js
  └── package.json
```

### 2️⃣ IAM Role with S3 Access

- Create a new **IAM Role** with:
  - Trusted entity: **EC2**
  - Permission: **AmazonS3ReadOnlyAccess**

> You'll attach this role to the EC2s via the Launch Template.

---

### 3️⃣ Create Target Group

- Go to **EC2 > Target Groups**
- Create a target group of type `Instance`
- Protocol: `HTTP`, Port: `80`
- Select your **VPC**
- Health check path: `/` (or your app route)

---

### 4️⃣ Launch Template

- Go to **EC2 > Launch Templates**
- Create a new template with:
  - AMI: **Amazon Linux 2023**
  - Instance type: `t2.micro`
  - Key pair: (create/select one for SSH access)
  - IAM Role: Select the role from Step 2
  - Security Group:
    - Inbound: `HTTP (80)`, `SSH (22)`
  - User data: Paste the following `init.sh` (after updating bucket name)

<details>
<summary>📜 <code>init.sh</code> (User Data)</summary>

```bash
#!/bin/bash

sudo dnf update -y
sudo dnf install -y git unzip curl

curl -fsSL https://rpm.nodesource.com/setup_18.x | bash -
sudo dnf install -y nodejs

sudo npm install -g pm2

cd /home/ec2-user

aws s3 cp s3://<your-bucket-name>/app.zip .

unzip -o app.zip -d app
cd app

npm install

sudo PORT=80 pm2 start /home/ec2-user/app/server.js --name node-app

pm2 save
pm2 startup systemd -u ec2-user --hp /home/ec2-user
```

</details>

Replace `<your-bucket-name>` with your actual S3 bucket name.

---

### 5️⃣ Auto Scaling Group (ASG)

- Go to **EC2 > Auto Scaling Groups**
- Create new ASG:
  - Use **Launch Template** created earlier
  - VPC + 3 AZs (for high availability)
  - Attach to the **Target Group** created earlier
  - Desired capacity: `3`, Min: `3`, Max: `3` (for test demo)

---

### 6️⃣ Application Load Balancer (ALB)

- Go to **EC2 > Load Balancers**
- Create **Application Load Balancer**
  - Type: `Internet-facing`
  - Scheme: `IPv4`
  - Listeners: HTTP on port 80
  - VPC: Use same as ASG
  - Subnets: Select 2–3 AZs
  - Add listener rule: Forward traffic to **Target Group**

Provisioning the ALB can take **4–6 minutes**.

---

## ✅ Testing

- Once ALB is active, copy its **Public DNS**
- Visit the URL in your browser:  
  `http://<alb-public-dns>`

- Refresh the page multiple times — you'll see responses from different EC2s (based on instance hostnames, IPs, or any logic you've added).

---

## 🧼 Optional Cleanup

To avoid charges:
- Delete the **Auto Scaling Group**
- Delete the **Launch Template**
- Delete the **ALB**
- Delete the **Target Group**
- Terminate EC2s (if any left)
- Delete the **S3 bucket** and uploaded `app.zip`
