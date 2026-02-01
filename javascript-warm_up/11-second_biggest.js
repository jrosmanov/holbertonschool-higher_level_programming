#!/usr/bin/node

const massiv = process.argv.slice(2);
if (massiv.length < 2) {
  console.log(0);
  process.exit(0);
}
massiv.sort((a, b) => b - a);
console.log(massiv[1]);
