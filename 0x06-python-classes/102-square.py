#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer or float.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number (float or integer)")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two squares are equal based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if two squares are not equal based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if one square is less than another based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the first square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if one square is less than or equal to another based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the first square's area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Check if one square is greater than another based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the first square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if one square is greater than or equal to another based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the first square's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
