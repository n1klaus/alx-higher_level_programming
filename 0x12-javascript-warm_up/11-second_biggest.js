#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(1);
} else {
  const myList = [];
  for (let i = 2; i < process.argv.length; i++) {
    myList.push(parseInt(process.argv[i]));
  }
  const compareFn = (a, b) => a - b;
  myList.sort(compareFn);
  console.log(myList.length - 2);
}
