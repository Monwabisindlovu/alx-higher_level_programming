#!/usr/bin/node
/**
 * Prints the number of movies where the character "Wedge Antilles" is present
 * The first argument is the API URL of the Star Wars API
 * Wedge Antilles whose character ID is 18 is used to filter the result
 * Uses the module 'request'
 */

if (process.argv.length === 3) {
  const request = require('request');
  const url = process.argv[2];
  request.get(url, function (e, r, b) {
    if (e) {
      throw e;
    } else {
      const a = JSON.parse(b);
      let n = 0;
      for (const i of a.results) {
        for (const c of i.characters) {
          if (c.endsWith('18/')) {
            n++;
          }
        }
      }
      console.log(n);
    }
  });
}
