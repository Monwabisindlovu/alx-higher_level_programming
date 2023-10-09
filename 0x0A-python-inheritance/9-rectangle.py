#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). This class includes methods to calculate the area and
print the description of a rectangle. This class does not require any modules
to be imported.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry and represents a rectangle.
    
    Attributes:
        __width: The width of the rectangle.
        __height: The height of the rectangle.
        
    Methods:
        __init__: Initializes a new Rectangle instance.
        area: Returns the area of the rectangle.
        __str__: Returns the string representation of the rectangle.
    """
    
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with width and height.
        
        Args:
            width: The width of the rectangle, must be a positive integer.
            height: The height of the rectangle, must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """
        Returns the area of the rectangle.
        
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        Returns the string representation of the rectangle.
        
        Returns:
            A string in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
