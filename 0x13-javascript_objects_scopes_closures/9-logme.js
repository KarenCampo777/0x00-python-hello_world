#!/usr/bin/node
// Count
let argCount = 0;
exports.logMe = function (item) {
  console.log(argCount + ': ' + item);
  argCount += 1;
};
