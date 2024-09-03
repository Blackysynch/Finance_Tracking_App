const express = require('express');
const app = express();
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');
const ObjectId = require('mongodb').ObjectId;

const url = 'mongodb://localhost:27017';
const dbName = 'financeTracker';

MongoClient.connect(url, function(err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const usersCollection = db.collection('users');
    const savingsCollection = db.collection('savings');

    app.use(bodyParser.json());
    app.use(express.static('public'));

    app.post('/users', (req, res) => {
      const userData = req.body;
      usersCollection.insertOne(userData, (err, result) => {
        if (err) {
          res.status(500).send({ message: 'Error creating user' });
        } else {
          res.send({ message: 'User created successfully' });
        }
      });
    });

    app.get('/users/:id', (req, res) => {
      const id = new ObjectId((link unavailable));
      usersCollection.findOne({ _id: id }, (err, user) => {
        if (err) {
          res.status(404).send({ message: 'User not found' });
        } else {
          res.send(user);
        }
      });
    });

    app.put('/users/:id', (req, res) => {
      const id = new ObjectId((link unavailable));
      const userData = req.body;
      usersCollection.updateOne({ _id: id }, { $set: userData }, (err, result) => {
        if (err) {
          res.status(500).send({ message: 'Error updating user' });
        } else {
          res.send({ message: 'User updated successfully' });
        }
      });
    });

    app.get('/savings/:id', (req, res) => {
      const id = new ObjectId((link unavailable));
      savingsCollection.find({ userId: id }).toArray((err, savings) => {
        if (err) {
          res.status(404).send({ message: 'Savings not found' });
        } else {
          res.send(savings);
        }
      });
    });

    const port = 3000;
    app.listen(port, () => {
      console.log(Server started on port ${port});
    });
  }
});
```