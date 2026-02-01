#!/usr/bin/node

const massivOfArguments = process.argv;

if (massivOfArguments[2] === undefined) {
  console.log('No argument');
} else {
  console.log(massivOfArguments[2]);
}
