# 🔁 Reverse Proxy with NGINX on Local WSL (Ubuntu)

This guide sets up a **Reverse Proxy** on your local machine using **NGINX** running on Ubuntu (WSL). We'll route incoming requests from port `80` to a backend server running on another port (e.g., `3000`).

---

## 📁 Project Structure

```
how-to-setup-x/
└── reverse-proxy/
    ├── backend/
    │   └── index.js
    └── nginx/
        └── nginx.conf
```

---

## 🔧 Step-by-Step Setup

### ✅ 1. Install NGINX on WSL

```bash
sudo apt update
sudo apt install nginx -y
```

---

### ✅ 2. Run Your Backend (Node.js Example)

```bash
cd reverse-proxy/backend
```

Example : **index.js:**

```js
const express = require("express");
const app = express();
const os = require("os");

app.get("/", (req, res) => {
  const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
  res.send(`<h2>From ${os.hostname()}</h2><p>Your IP: ${ip}</p>`);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

**Install dependencies:**
```bash
npm install express
node server.js
```

---

### ✅ 3. Configure NGINX as Reverse Proxy

```bash
sudo nano /etc/nginx/sites-available/default
```

**Replace the `server` block with:**
```nginx
server {
    listen 80;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Then:

```bash
sudo nginx -t           # Test config
sudo systemctl restart nginx
```

---

## 🚀 Test It

In your terminal or browser:

```bash
curl http://localhost
```

Expected output:

```
<h2>From <hostname></h2><p>Your IP: <your_ip></p>
```

---

## 🛑 To Stop NGINX

```bash
sudo systemctl stop nginx
```