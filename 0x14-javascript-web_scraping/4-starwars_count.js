#!/usr/bin/node
/* A script that prints the number of movies where the character "Wedge Antilles" is present. */

const request = require('request');

// Get the Star Wars API URL from the command line arguments
const apiUrl = process.argv[2];

// Define the character ID for "Wedge Antilles"
const characterId = 18;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Filter films where "Wedge Antilles" is present
    const filmsWithWedge = filmsData.results.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });

    // Print the number of films with "Wedge Antilles"
    console.log(filmsWithWedge.length);
  }
});

