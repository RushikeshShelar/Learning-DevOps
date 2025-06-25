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