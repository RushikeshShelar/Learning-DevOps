const express = require("express");
const os = require("os");
const app = express();

app.get("/", (req, res) => {
    const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
    res.send(`
    <h2>Hello from backend 1: ${os.hostname()} 🚀</h2>
    <p>Your IP: ${ip}</p>
  `);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Running on ${os.hostname()} - Port ${port}`);
});