#!/usr/bin/node
/* A script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the body response to the specified file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});

