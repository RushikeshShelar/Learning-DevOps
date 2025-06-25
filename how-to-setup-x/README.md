# 🧩 Infrastructure Components – Local and EC2 Setups

This folder contains a collection of demos and configuration files that illustrate how to set up essential components in a modern infrastructure stack. These setups are designed to work either **locally** using tools like Nginx and Squid, or on **cloud instances** like AWS EC2. The goal is to understand the role, behavior, and configuration of core building blocks in DevOps: Load Balancers, Proxies, Caching Layers, and Firewalls.

---

## ⚖️ Load Balancer

A **Load Balancer** is a key component in distributed systems that helps distribute incoming traffic evenly across multiple backend servers. Its main objective is to improve the availability, scalability, and fault tolerance of an application. If one of the servers goes down, the load balancer automatically reroutes traffic to the healthy ones. This not only prevents overload on a single server but also ensures that services remain available to users without interruption.

Locally, **Nginx** can be configured to act as a reverse proxy-based load balancer, using methods like **round-robin**, **least connections**, or **IP hash** to decide how to distribute incoming requests. This setup simulates how cloud-based load balancers (like AWS ALB or NLB) behave, helping you understand traffic distribution strategies at a foundational level.

- **High availability** – if one server goes down, traffic is routed to others.
- **Scalability** – handles more requests by adding more backend servers.
- **Improved performance** – distributes workload evenly.

### 🧪 Local Load Balancer using Nginx

In this demo, Nginx is configured to act as a basic round-robin **reverse proxy load balancer** for multiple backend servers (like Node.js apps running on different ports or IPs).


➡️ [See load balancer setup](./load-balancer)

---

## 🛰️ Forward Proxy

A **Forward Proxy** is placed between a client (like your browser or internal system) and the internet. Its primary job is to act on behalf of the client, forwarding requests to external servers and returning responses back. It is commonly used in corporate environments to control internet usage, monitor traffic, and apply content filtering policies.

- **Content filtering**
- **Caching web content**
- **Monitoring and control**
- **Masking client identity (IP address)**

Common tools include **Nginx**, **Squid**, **Tinyproxy**, and **Privoxy**.


➡️ [See forward proxy setup](./forward-proxy)

---

## 🔁 Reverse Proxy

A **Reverse Proxy** is positioned in front of one or more backend servers and handles incoming client requests by forwarding them to the appropriate server. It essentially acts on behalf of the server, hiding its identity from the client. Reverse proxies are widely used in production to serve static content, route dynamic traffic, perform SSL termination, apply rate limiting, and improve security.

Used for:

- **Load balancing**
- **TLS/SSL termination**
- **Caching & compression**
- **Security / hiding server details**

### 🔄 Reverse Proxy vs Load Balancer

- A **Load Balancer** distributes traffic across **multiple servers**.
- A **Reverse Proxy** can forward traffic to **one or more servers**, but focuses more on **security, TLS offloading, and routing logic**.
- **Nginx** can serve as both a reverse proxy and a load balancer (config-dependent).

This demo showcases how to set up a reverse proxy using Nginx that forwards traffic to a backend Node.js or Python app running on a different port or server.

➡️ [See reverse proxy setup](./reverse-proxy)

---

## 🧠 Caching Server

A **Caching Server** stores frequently accessed content temporarily to reduce backend load and improve request-response times. Instead of going all the way to the origin server for every request, the cache layer serves static or repeat content from memory or disk, making web applications much faster and more efficient.

- Placed **between clients and the application server**
- Can cache based on request path, headers, status codes, etc.
- Reduces backend load, improves speed, and cuts bandwidth usage

In this setup, we use **Nginx** with `proxy_cache` directives to enable HTTP caching of upstream content.

➡️ [See cache server setup](./cache-server)

---

## 🔐 Firewalls

A **Firewall** is a security mechanism that controls network traffic to and from systems based on predefined rules. Its role is to block unauthorized access while allowing legitimate communication. Firewalls can operate at different layers — either on the host machine (using tools like `ufw` or `iptables`) or at the network level in cloud environments (such as **Security Groups** or **Network ACLs** in AWS).

Host-level firewalls are configured directly on Linux machines using command-line tools, and can control both incoming and outgoing traffic. In contrast, AWS security groups act as virtual firewalls for EC2 instances, allowing or blocking traffic based on port, IP, and protocol. Unlike NACLs (Network Access Control Lists), which evaluate both inbound and outbound rules statelessly, security groups are **stateful** and primarily focus on inbound traffic management.

There are 2 types commonly used:

1. **Host-level Firewalls** (e.g., `ufw`, `iptables`) – configured on the operating system.
2. **Cloud-level Firewalls** (e.g., **AWS Security Groups**) – control traffic at the **network level**.

### Key Differences:

| Layer | Example       | Checks             |
| ----- | ------------- | ------------------ |
| NACLs | AWS VPC       | Inbound + Outbound |
| SGs   | EC2 Instances | Inbound-only       |
| UFW   | Ubuntu/Local  | Both directions    |


This section includes hands-on demos of firewall rules using `ufw` for local Linux systems.

➡️ [See firewall setup](./firewall)

## 📦 Summary

| Component     | Tool Used | Demo Folder                      |
| ------------- | --------- | -------------------------------- |
| Load Balancer | Nginx     | [load-balancer](./load-balancer) |
| Forward Proxy | Nginx     | [forward-proxy](./forward-proxy) |
| Reverse Proxy | Nginx     | [reverse-proxy](./reverse-proxy) |
| Cache Server  | Nginx     | [cache-server](./cache-server)   |
| Firewall      | UFW / SGs | [firewall](./firewall)           |

---

> 💡 These examples help simulate production-like setups locally or on EC2 for deeper DevOps & networking understanding.