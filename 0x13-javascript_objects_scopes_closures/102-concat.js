#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (errA, dataA) => {
  if (errA) {
    console.error(errA.message);
    process.exit(1);
  }

  fs.readFile(fileB, 'utf8', (errB, dataB) => {
    if (errB) {
      console.error(errB.message);
      process.exit(1);
    }

    const concatenatedContent = dataA + dataB;

    fs.writeFile(fileC, concatenatedContent, (errC) => {
      if (errC) {
        console.error(errC.message);
        process.exit(1);
      }

      console.log(`The content of ${fileA} and ${fileB} has been successfully concatenated to ${fileC}`);
    });
  });
});

