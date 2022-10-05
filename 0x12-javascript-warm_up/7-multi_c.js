#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

let num = ~~process.argv[2];
if (!isNaN(num)) {
  while (num > 0) {
    num--;
    console.log('C is fun');
  }
}
process.exit(1);
