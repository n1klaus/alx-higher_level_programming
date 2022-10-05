#!/usr/bin/node

const list = require('./100-data').list;
let index = 0;

const myList = [...list];
function counter (a) { return a * index++; }
console.log(list);
console.log(myList.map(function (a) { return counter(a); }));
