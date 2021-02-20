#!/usr/bin/node
// C is fun?
Class Square extends require('./5-square') {
  charPrint (obj) {
    if (obj === undefined) {
      obj = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(obj.repeat(this.width));
    }
  }
}
module.exports = Square;
