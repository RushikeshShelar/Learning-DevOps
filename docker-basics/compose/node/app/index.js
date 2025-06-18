const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});


app.get('/', (req, res) => {
    console.log(process.env.MONGO_URI);
    res.send('Hello from the Express app!');
});

app.listen(3000, () => {
    console.log('Express app listening on port 3000');
});