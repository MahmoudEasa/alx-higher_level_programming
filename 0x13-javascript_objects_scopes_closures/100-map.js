#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((i, e) => {
  return (i * e);
});
console.log(newList);
