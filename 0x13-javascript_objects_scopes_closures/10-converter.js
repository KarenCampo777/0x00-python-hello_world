#!/usr/bin/node
// Converts number
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
