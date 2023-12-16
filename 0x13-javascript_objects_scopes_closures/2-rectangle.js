#!/usr/bin/node
// Class Rectangle that defines a rectangle
class Rectangle {
  // Constructor that takes 2 arguments w and h
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    }
    // Otherwise, create an empty object
  }
}

// Export the class
module.exports = Rectangle;

