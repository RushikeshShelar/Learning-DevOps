# 🌐 Forward Proxy Setup using Nginx

This guide explains how to set up a **Forward Proxy Server** using **Nginx** on Linux (Ubuntu or Amazon EC2). A forward proxy allows you to route your requests through this server, effectively masking your original IP address.

---

## ✅ What You'll Achieve

- Setup a Linux server (local or EC2) with Nginx acting as a forward proxy
- Route outgoing HTTP requests via the proxy
- Optional: Secure proxy using IP restriction or Basic Auth

---

## 🧰 Prerequisites

- Ubuntu 22.04 LTS / Amazon Linux 2023
- Nginx installed
- Public IP address if testing from remote machine
- (Optional) SSH access to an EC2 instance

---

## 📦 Step 1: Install Nginx

### Ubuntu:
```bash
sudo apt update
sudo apt install nginx -y
```

### Amazon Linux:
```bash
sudo yum update -y
sudo yum install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

---

## ⚙️ Step 2: Configure Nginx as Forward Proxy

Edit the Nginx configuration:

```bash
sudo vim /etc/nginx/nginx.conf
```

Inside the `http {}` block, add:

```nginx
server {
    listen 8888;

    location / {
        resolver 8.8.8.8;
        proxy_pass $scheme://$http_host$request_uri;

        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

> 🔁 Port `8888` is arbitrary. You can change it if needed.

---

## 🔐 (Optional) Step 3: Secure Your Proxy

### Restrict by IP (Recommended)
Add inside `location /`:
```nginx
allow YOUR.IP.ADD.RESS;
deny all;
```

## ♻️ Step 4: Restart Nginx

```bash
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🧪 Step 5: Test the Proxy

### From the same machine:
```bash
curl -x http://localhost:8888 http://example.com
```

### From another machine (use server’s IP):
```bash
curl -x http://<EC2-IP>:8888 http://example.com
```

> Add `-v` to see headers and connection logs:
```bash
curl -x http://<EC2-IP>:8888 http://example.com -v
```

---

## 🧠 How It Works

When you set Nginx to listen as a proxy on port `8888`, it accepts client requests and forwards them to the target server. It then returns the server's response back to the client.

---

## 🚨 Warnings

- **Never leave an open proxy** in public! Secure it with IP restrictions or password.
- This setup supports only **HTTP** traffic by default (not HTTPS CONNECT tunneling).

---
