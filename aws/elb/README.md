# ⚖️ AWS Elastic Load Balancers (ELB) & Auto Scaling

---

## 🧠 What is a Load Balancer?

A **Load Balancer** is a system that automatically distributes incoming application traffic across multiple servers or instances to ensure **high availability**, **reliability**, and **performance**. It prevents any single server from becoming a bottleneck or point of failure.

In a real-world analogy, imagine a load balancer as a traffic police officer at a busy intersection who redirects cars to different lanes to avoid congestion.

Without a load balancer:
- A single EC2 instance handles all requests → risk of overload.

With a load balancer:
- Requests are evenly spread across multiple instances → better performance & fault tolerance.

---

## 🧰 Types of Load Balancers (in general)

There are several types of load balancers based on **layer of operation** and **deployment context**:

| Type                                | Layer                | Description                                                                            |
| ----------------------------------- | -------------------- | -------------------------------------------------------------------------------------- |
| **Application Load Balancer (ALB)** | Layer 7 (HTTP/HTTPS) | Smart routing based on URLs, headers, or cookies. Ideal for web applications.          |
| **Network Load Balancer (NLB)**     | Layer 4 (TCP/UDP)    | Extremely fast, works at connection level. Good for low latency, high throughput apps. |
| **Gateway Load Balancer (GWLB)**    | Layer 3 (IP)         | Used for network appliances like firewalls, packet inspection, etc.                    |

---

## ⚙️ Load Balancing Algorithms

Load balancers follow different algorithms to distribute traffic:

- **Round Robin**: Default and most common; sends requests to instances in a rotating fashion.
- **Least Connections**: Sends traffic to the instance with the fewest active connections.
- **IP Hash**: Uses client IP to determine which instance handles the request (useful for session stickiness).

AWS ALB uses Round Robin by default for HTTP, while NLB distributes based on flow hash algorithms.

---

## 🚀 Launch Templates

A **Launch Template** defines the configuration of an EC2 instance that can be launched automatically by services like **Auto Scaling Groups (ASG)**. It includes:

- AMI ID (OS)
- Instance type
- Key pair
- Security groups
- User data script
- IAM roles

### Why use Launch Templates?

They make it easy to consistently create EC2 instances with the same configuration, especially when used with ASG for scaling.

### Example Use Case:
You're running a web app and want to automatically scale it across multiple EC2s — you'll define a Launch Template once and reuse it every time a new EC2 needs to be spun up.

---

## 📈 Auto Scaling Groups (ASG)

An **Auto Scaling Group** is a collection of EC2 instances that can automatically scale in or out based on **demand** (like CPU usage or number of requests).

ASG uses:
- **Launch Template** (what to launch)
- **Scaling policies** (when to scale)
- **Target Group** (where to send traffic)
- **Subnets/VPC** (where to place the instances)

### Example Use Case:
You define min: 2, max: 5 instances in an ASG. Based on CPU > 70%, AWS automatically adds new EC2s and removes them when traffic drops.

ASG ensures **resiliency** and **cost-efficiency**.

---

## 🧩 Target Groups

A **Target Group** is a logical grouping of EC2 instances (or containers, Lambda, IPs) that receive traffic from a Load Balancer.

Each Load Balancer forwards traffic to its registered Target Group(s). Targets are monitored using **health checks**.

### Health Checks:
- You define a protocol and path (e.g., HTTP `/health`) to check each target’s availability.
- If a target fails repeatedly, it’s removed from routing temporarily.

Example:
You can have one target group for `/api` routes and another for `/frontend`, each routed via ALB rules.

---

## ☁️ AWS Elastic Load Balancers (ELB)

**ELB** is a managed service by AWS that includes all types of load balancers. AWS automatically manages the provisioning, scaling, and high availability of the load balancer infrastructure.

Three main types of ELBs:

---

## 🌐 Application Load Balancer (ALB)

- Operates at **Layer 7 (HTTP/HTTPS)**
- Best for web applications that require **advanced routing** (like path-based or host-based)
- Supports **content-based routing**, SSL termination, WebSockets, and redirects.

### Example Scenario:
- `/api` → routed to microservice backend
- `/frontend` → routed to React app

### Key Features:
- Path-based routing
- Host-based routing
- Header-based routing
- Sticky sessions (via cookies)
- Target types: EC2, IP, Lambda, ECS services

---

## 🔌 Network Load Balancer (NLB)

- Operates at **Layer 4 (TCP/UDP)**
- Designed for **high performance** and **low latency**
- Capable of handling millions of requests per second
- Can preserve the **client IP address**

### Use Case:
For financial applications or games where TCP latency is critical.

NLB doesn’t understand application-level data; just forwards packets at connection level.

---

## 🔐 Gateway Load Balancer (GWLB)

- Operates at **Layer 3 (IP)**
- Primarily used for **third-party virtual appliances** like firewalls, intrusion detection systems, etc.
- Allows you to insert transparent, inline appliances without modifying traffic flow

Use Case:
Deploying a virtual firewall across VPCs for inspection before traffic hits ALB/NLB.

---

## 📦 Putting It All Together: Full Architecture Example

Imagine you're deploying a modern scalable app:
- Use **Launch Template** to define EC2 app instances
- Use **ASG** to auto-scale EC2s based on demand
- Create **Target Group** linked with the ASG
- Use **ALB** to route traffic from `/api` to app instances
- Optionally use **CloudWatch + Alarm** to scale up/down ASG
- Secure everything using **Security Groups**, **NACLs**, and **SSL** if needed

---