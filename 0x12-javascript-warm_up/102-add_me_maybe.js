#!/usr/bin/node

function addMeBaby (number, theFunction) {
  const num = ++number;
  theFunction(num);
}

module.exports = { addMeMaybe: addMeBaby };
