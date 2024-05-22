#!/ust/bin/node

const request = require('request');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, async (err, res, body) => {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  for (const charUrl of chars) {
    request(charUrl, async (err, _, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
