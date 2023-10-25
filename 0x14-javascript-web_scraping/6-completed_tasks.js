#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const result = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (result[data[i].userId]) {
          result[data[i].userId]++;
        } else {
          result[data[i].userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
