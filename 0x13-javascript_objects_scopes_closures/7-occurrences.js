#!/usr/bin/node
// Ocurrences
exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};