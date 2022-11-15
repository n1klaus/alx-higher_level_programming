#!/usr/bin/node
const fs = require('fs');

const file = process.argv[1];

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data.toString());
});
