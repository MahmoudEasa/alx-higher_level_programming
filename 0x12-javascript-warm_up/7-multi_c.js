#!/usr/bin/node

let i;
const argv = require('process').argv;

const num = Number(argv[2]);

if (num) {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
