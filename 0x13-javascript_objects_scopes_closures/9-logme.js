#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  function counter () {
    console.log(count++ + ': ' + item);
  }
  counter();
};
