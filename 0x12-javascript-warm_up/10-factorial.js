#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const f = factorial(parseInt(process.argv[2]));
console.log(f);
