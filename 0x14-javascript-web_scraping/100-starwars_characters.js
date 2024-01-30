#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Displays one character name per line
 * Uses the Star Wars API
 * Uses the module 'request'
 */

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the Star Wars API endpoint for films
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API for the specified film
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const filmData = JSON.parse(body);

    // Print all characters of the movie
    filmData.characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});

