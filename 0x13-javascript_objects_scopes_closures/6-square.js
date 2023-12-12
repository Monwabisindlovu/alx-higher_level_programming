#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  charPrint(c) {
    // If c is undefined, use the character X
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the specified character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareWithCharPrint;

