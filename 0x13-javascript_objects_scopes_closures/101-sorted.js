#!/usr/bin/node

const dict = require('./101-data').dict;

const userByOccurrence = {};


for (const userId in dict) {
  const occurrences = dict[userId];

  if (!userByOccurrence[occurrences]) {
    userByOccurrence[occurrences] = [];
  }

  userByOccurrence[occurrences].push(userId);
}

console.log(userByOccurrence);
