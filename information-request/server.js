const express = require('express');
const app = express();
const { MongoClient, ServerApiVersion } = require('mongodb');

require('dotenv').config();

const port = process.env.PORT || 3030;
const dburi = process.env.DATABASE_URI;
const client = new MongoClient(dburi, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });

// middleware
app.use(express.json());
app.use(express.urlencoded( { extended: true } ));

// create routes
app.get('/api/applicants', async (req, res) => {
    const collection = client.db('applications').collection('applicants');
    const data = await collection.find().toArray();
    res.status(200).json(data);
});

// create POST API route
app.post('/api/applicants', async (req, res) => {
    console.log('You posted from a form!');
    console.log(req.body);

    const data = { ...req.body, dateOfApplication: new Date() }; // ... copies whatever i have in an array and makes a deep copy

    const collection = client.db("applications").collection("applicants");
    try {
        await collection.insertOne(data);
    } catch (error) {
        console.log(error.message);
    }
    res.status(201);
    res.redirect('/list-applicants.html');
});

app.post('/api/submitted', async (req, res) => {
    console.log('You posted from a form!');
    console.log(req.body);

    const data = { ...req.body, dateOfApplication: new Date() }; // ... copies whatever i have in an array and makes a deep copy

    const collection = client.db("applications").collection("applicants");
    try {
        await collection.insertOne(data);
    } catch (error) {
        console.log(error.message);
    }
    res.status(201);
    res.redirect('/submitted.html');
});

// catch all routes
app.use(express.static('public'));

app.listen(port, () => {
    console.log('App running on http://localhost:' + port);
    // connect to database

    client.connect(err => {
        if (err) {
            console.log('Error!', err.message);
            return;
        }

        console.log('Connected to database successfully!');
    });
});

//gracefully close db connection
const cleanup = (event) => {
    console.log('Database connection closed');
    client.close();
    process.exit();
}

process.on('SIGINT', cleanup);
process.on('SIGTERM', cleanup);