#!/usr/bin/node

const myArgs = process.argv;
for (let x = 2; x < myArgs.length; x++) {
  if (isNaN(myArgs[x])) {
    console.log('Not a number');
  } else {
    console.log('My number:', ~~myArgs[x]);
  }
}
process.exit(1);
