#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request(data[i], (err, res, body) => {
        console.log(err || JSON.parse(body).name);
      });
    }
  }
});
