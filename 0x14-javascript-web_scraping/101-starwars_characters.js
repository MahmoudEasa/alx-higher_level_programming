#!/usr/bin/node

const request = require('request');
const util = require('util');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const requestPromise = util.promisify(request);

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      const response = await requestPromise(data[i]);
      try {
        console.log(JSON.parse(response.body).name);
      } catch (err) {
        console.log(err);
      }
    }
  }
});
