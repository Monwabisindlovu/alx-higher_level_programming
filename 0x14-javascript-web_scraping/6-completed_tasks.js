#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only prints users with completed tasks
 * Uses the module 'request'
 */

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Iterate through the todos and count completed tasks for each user
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId] === undefined) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    // Print the results
    console.log(completedTasksByUser);
  }
});

