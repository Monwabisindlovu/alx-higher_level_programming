#!/usr/bin/python3
class Square:
    """Class Square that defines a square with private instance attributes size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square.

        Args:
            value (int): The size of the Square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the Square.

        Args:
            value (tuple): The position of the Square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
            return
        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print()

    def __str__(self):
        """Returns a string representation of the square."""
        if self.__size == 0:
            return ""
        [print() for _ in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            if i < self.__size - 1:
                print()
        return ""
