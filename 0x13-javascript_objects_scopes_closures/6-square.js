#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let output = '';
    let ch;
    if (c) {
      ch = c;
    } else {
      ch = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        output += ch;
      }
      console.log(output);
      output = '';
    }
  }
};
