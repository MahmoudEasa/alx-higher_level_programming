#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';
const id = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    for (let i = 0; i < data.length; i++) {
      for (let j = 0; j < data[i].films.length; j++) {
        if (data[i].films[j].endsWith('/' + id + '/')) {
          console.log(data[i].name);
        }
      }
    }
  }
});
