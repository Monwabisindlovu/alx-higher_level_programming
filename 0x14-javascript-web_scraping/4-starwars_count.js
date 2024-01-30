#!/usr/bin/node
/* A script that prints the number of movies where the character "Wedge Antilles" is present. */

const request = require('request');

// Get the Star Wars API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the Star Wars API URL');
  process.exit(1);
}

// Define the character ID for "Wedge Antilles"
const characterId = 18;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      // Parse the JSON response
      const filmsData = JSON.parse(body);

      // Validate the response
      if (!filmsData || !Array.isArray(filmsData.results)) {
        console.error('Invalid API response');
        return;
      }

      // Filter films where "Wedge Antilles" is present
      const filmsWithWedge = filmsData.results.filter((film) => {
        return Array.isArray(film.characters) && film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
      });

      // Print the number of films with "Wedge Antilles"
      console.log(filmsWithWedge.length);
    } catch (err) {
      console.error('Error parsing API response:', err);
    }
  }
});

