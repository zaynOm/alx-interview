#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, async (err, res, body) => {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  for (const charUrl of chars) {
    const { name } = await new Promise((resolve, reject) => {
      request(charUrl, async (err, _, body) => {
        if (err) throw err;
        resolve(JSON.parse(body));
      });
    });
    console.log(name);
  }
});
