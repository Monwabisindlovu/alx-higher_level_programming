#!/usr/bin/python3
class Square:
    """Class Square that defines a square with a private instance attribute size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
