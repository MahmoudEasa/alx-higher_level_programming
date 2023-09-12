#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let output = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        output += 'X';
      }
      console.log(output);
      output = '';
    }
  }
};
