#!/usr/bin/node

function callMeBaby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { callMeMoby: callMeBaby };
