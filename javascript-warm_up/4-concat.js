#!/usr/bin/node

const massivOfArguments = process.argv;

if (massivOfArguments[2] !== undefined && massivOfArguments[3] !== undefined) {
  console.log(`${massivOfArguments[2]} is ${massivOfArguments[3]}`);
} else if (massivOfArguments[2] !== undefined && massivOfArguments[3] === undefined) {
  console.log(`${massivOfArguments[2]} is ${undefined}`);
} else if (massivOfArguments[2] === undefined && massivOfArguments[3] === undefined) {
  console.log(`${undefined} is ${undefined}`);
}
