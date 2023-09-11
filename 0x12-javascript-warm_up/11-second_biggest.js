#!/usr/bin/node

let argv = require('process').argv;
const argvLen = argv.length;

function sortArray (argv, len, start) {
  let i, tmp;
  let sorted = 0;

  while (!sorted) {
    sorted = 1;

    for (i = start; i < len - 1; i++) {
      if (+argv[i] > +argv[i + 1]) {
        tmp = argv[i];
        argv[i] = argv[i + 1];
        argv[i + 1] = tmp;
        sorted = 0;
      }
    }
  }
  return (argv);
}

if (argvLen < 4) {
  console.log(0);
} else {
  argv = sortArray(argv, argvLen, 2);
  console.log(argv[argvLen - 2]);
}
