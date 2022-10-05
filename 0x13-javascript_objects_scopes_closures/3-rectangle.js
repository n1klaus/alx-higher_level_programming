#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let buffer = '';
      for (let w = 0; w < this.width; w++) {
        buffer += 'X';
      }
      console.log(buffer);
    }
  }
}

module.exports = Rectangle;
