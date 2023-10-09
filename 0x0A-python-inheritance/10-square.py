#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle
(9-rectangle.py). This class includes a method to calculate the area of a
square. This class does not require any modules to be imported.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle and represents a square.
    
    Attributes:
        __size: The size of the square.
        
    Methods:
        __init__: Initializes a new Square instance.
        area: Returns the area of the square.
    """
    
    def __init__(self, size):
        """
        Initializes a new Square instance with size.
        
        Args:
            size: The size of the square, must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        
    def area(self):
        """
        Returns the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2
