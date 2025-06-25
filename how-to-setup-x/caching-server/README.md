# 🧠 NGINX Caching Server Setup

This guide sets up a **Caching Server using NGINX** to cache responses from a backend server (e.g., Node.js app) to improve performance and reduce repeated load on the origin server.

---

## 📌 What is a Caching Server?

A caching server stores responses (like HTTP pages or API responses) and serves them quickly without hitting the backend every time.

---

## 🛠️ Tech Stack

- Ubuntu 22.04 / Amazon Linux
- Nginx
- Node.js + Express (as a sample backend)

---

## 📦 Step 1: Install Nginx

```bash
sudo apt update
sudo apt install nginx -y
```

---

## 🔧 Step 2: Start a Backend Server (Node.js + Express)

```bash
cd backend
npm install express
```

Create a file `index.js`:

```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  const time = new Date();
  res.send(`Hello! Time is ${time}`);
});

app.listen(3000, () => console.log("Backend running on port 3000"));
```

Run the server:

```bash
node index.js
```

---

## ⚙️ Step 3: Configure NGINX for Caching

Edit the default NGINX config file:

```bash
sudo vim /etc/nginx/sites-available/default
```

Replace content with:

```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=STATIC:10m inactive=60m use_temp_path=off;

server {
    listen 80;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;

        proxy_cache STATIC;
        proxy_cache_valid 200 302 10s;
        proxy_cache_use_stale error timeout updating;

        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

- `proxy_cache_path`: where the cache will be stored.
- `keys_zone`: defines memory zone for caching.
- `proxy_cache_valid`: cache success responses for 10s.
- `X-Cache-Status`: Shows if response was a `HIT` or `MISS`.

---

## ✅ Step 4: Restart NGINX

```bash
sudo nginx -t       # test config
sudo systemctl restart nginx
```

---

## 🧪 Step 5: Test the Cache

Make repeated requests:

```bash
curl -i http://localhost
```

Output headers will show:

- `X-Cache-Status: MISS` on first request
- `X-Cache-Status: HIT` if repeated within 10 seconds

---

## 📌 Notes

- This cache only works for responses with `200` or `302` status codes.
- Tune `proxy_cache_valid`, `inactive`, and `use_temp_path` as needed.
- Make sure NGINX has permission to write to `/var/cache/nginx`.
