#!/usr/bin/node

const SquareSuper = require('./5-square');

class Square extends SquareSuper {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let row = 0; row < this.height; row++) {
      let strBuffer = '';
      for (let col = 0; col < this.width; col++) {
        strBuffer += c;
      }
      console.log(strBuffer);
    }
  }
}

module.exports = Square;
