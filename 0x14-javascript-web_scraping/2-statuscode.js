#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  console.log('code: ', (err || res.statusCode));
});
