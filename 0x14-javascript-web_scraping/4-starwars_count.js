#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  const results = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(err || count);
});
