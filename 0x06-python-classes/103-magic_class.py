#!/usr/bin/python3

import math

class MagicClass:
    """A class that emulates the provided Python bytecode operations."""

    def __init__(self, radius=0):
        """Initialize the MagicClass instance."""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculate the area of a circle with the given radius."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of a circle with the given radius."""
        return 2 * math.pi * self.__radius
