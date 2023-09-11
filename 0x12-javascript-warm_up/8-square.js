#!/usr/bin/node

let i, j;
let result;
const argv = require('process').argv;

const num = Number(argv[2]);

if (num) {
  result = '';

  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      result += 'X';
    }
    console.log(result);
    result = '';
  }
} else {
  console.log('Missing size');
}
