# 🌀 NGINX Load Balancer – Local Setup Guide

This guide helps you set up **NGINX as a Load Balancer** on your **local WSL (Ubuntu)** system to balance requests between two simple Node.js backend servers.

## 📁 Folder Structure

```
how-to-setup-x/
└── load-balancer/
    ├── backend1/
    │   └── server.js
    ├── backend2/
    │   └── server.js
    └── nginx/
        └── nginx.conf
```

---

## 🔧 Step-by-Step Setup

### 1. Install NGINX (if not already)

```bash
sudo apt update
sudo apt install nginx -y
```

### 2. Create Backend Servers

`server.js` in both `backend1/` and `backend2/`:

**Example `server.js`:**

```js
const express = require("express");
const os = require("os");
const app = express();

app.get("/", (req, res) => {
  const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
  res.send(`
    <h2>Hello from ${os.hostname()} 🚀</h2>
    <p>Your IP: ${ip}</p>
  `);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Running on ${os.hostname()} - Port ${port}`);
});
```

Install dependencies:

```bash
cd backend1 && npm init -y && npm install express && cd ..
cd backend2 && npm init -y && npm install express && cd ..
```

Run both servers on different ports:

```bash
PORT=3001 node backend1/server.js
PORT=3002 node backend2/server.js
```

### 3. Update NGINX Config

Update the  `/etc/nginx/sites-available/deafult` file;
```bash
sudo nano /etc/nginx/sites-available/deafult
```
Replace the contents with the following.
```nginx
upstream backend {
        server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}

server {
    listen 8080;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 4. Run NGINX with Your Config

Start/Restart the nginx Service

```bash
sudo systemctl start nginx
```
```bash
sudo systemctl restart nginx
```

> ✅ This runs NGINX with your custom config. Make sure port `8080` is free.

---

## ✅ Test

Visit [http://localhost:8080](http://localhost:8080) in your browser or run:

```bash
curl localhost:8080
```

You should see alternating responses from both servers (`backend1`, `backend2`) on each refresh.

---

## 🛑 To Stop NGINX

```bash
sudo systemctl stop nginx
```
