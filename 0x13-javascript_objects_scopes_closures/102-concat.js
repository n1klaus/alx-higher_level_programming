#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 5) {
  process.exit(1);
}
const file1 = fs.readFileSync(process.argv[2]).toString();
const file2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], file1 + file2);
process.exit(1);
