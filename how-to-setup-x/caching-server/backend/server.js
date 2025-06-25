const express = require("express");
const app = express();

app.get("/", (req, res) => {
    const time = new Date();
    res.send(`Hello! Time is ${time}`);
});

app.listen(3000, () => console.log("Server on port 3000"));
