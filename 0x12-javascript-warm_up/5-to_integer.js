#!/usr/bin/node

const argv = require('process').argv;

const num = Number(argv[2]);

if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
