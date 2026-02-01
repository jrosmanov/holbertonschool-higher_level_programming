#!/usr/bin/node

const number = Number(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
