#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Missing size');
  process.exit(1);
} else {
  const num = ~~process.argv[2];
  if (!isNaN(num)) {
    if (num > 0) {
      for (let row = 0; row < num; row++) {
        let buffer = '';
        for (let col = 0; col < num; col++) {
          buffer += 'X';
        }
        console.log(buffer);
      }
    }
  } else {
    console.log('Missing size');
  }
}
process.exit(1);
