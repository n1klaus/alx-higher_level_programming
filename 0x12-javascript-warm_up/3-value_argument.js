#!/usr/bin/node

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  process.stderr.write('No argument\n');
}
process.exit(1);
