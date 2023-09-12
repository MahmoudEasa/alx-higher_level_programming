#!/usr/bin/node

const dict = require('./101-data.js').dict;

const ids = {};
let arr = [];
const output = {};
let found = 0;

for (const id in dict) {
  for (const id2 in ids) {
    if (dict[id] === ids[id2]) {
      found = 1;
    }
  }

  if (!found) {
    ids[id] = dict[id];
  }
  found = 0;
}

for (const i in ids) {
  for (const j in dict) {
    if (dict[j] === ids[i]) {
      arr.push(j);
    }
  }
  output[ids[i]] = arr;
  arr = [];
}

console.log(output);
