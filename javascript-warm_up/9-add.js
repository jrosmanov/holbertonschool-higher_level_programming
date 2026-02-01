#!/usr/bin/node

const numberFirst = Number(process.argv[2]);
const numberSecond = Number(process.argv[3]);

function add (one, two) {
  const result = one + two;
  return result;
}

if (Number.isNaN(numberFirst) || Number.isNaN(numberSecond)) {
  console.log(NaN);
} else {
  console.log(add(numberFirst, numberSecond));
}
