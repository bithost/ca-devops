const express = require('express');
const fs = require('fs');

const app = express();

// Define a route to read and display the secret
app.get('/showSecret', (req, res) => {
  // Read the secret file
  fs.readFile('/run/secrets/secret.txt', 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading secret file:', err);
      res.status(500).send('Error reading secret file');
    } else {
      console.log('Secret:', data);
      res.send(`The secret is: ${data}`);
    }
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
