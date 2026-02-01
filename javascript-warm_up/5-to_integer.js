#!/usr/bin/node

const massivOfArguments = process.argv;
const value = Number(massivOfArguments[2]);

if (Number.isNaN(value)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${massivOfArguments[2]}`);
}
