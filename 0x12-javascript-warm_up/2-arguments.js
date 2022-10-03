#!/usr/bin/node

if (process.argv.length === 2) {
  process.stderr.write('No argument\n');
} else if (process.argv.length === 3) {
  process.stderr.write('Argument found\n');
} else {
  process.stderr.write('Arguments found\n');
}
process.exit(1);
