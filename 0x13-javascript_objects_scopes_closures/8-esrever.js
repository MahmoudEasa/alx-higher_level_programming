#!/usr/bin/node

exports.esrever = function (list) {
  const listLen = list.length;
  let j = listLen - 1;
  for (let i = 0; i < listLen / 2; i++) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    j--;
  }
  return (list);
};
