#!/usr/bin/node

exports.converter = function (base) {
  return function getNumber (num) {
    return num.toString(base);
  };
};
