#!/usr/bin/node
/* A script that prints the title of a Star Wars movie. */

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Print the title of the movie
    console.log(movieData.title);
  }
});

