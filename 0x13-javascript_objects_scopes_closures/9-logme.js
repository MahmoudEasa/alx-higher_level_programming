#!/usr/bin/node

let numArg = 0;

exports.logMe = function (item) {
  console.log(`${numArg++}: ${item}`);
};
