#!/usr/bin/python3

class Square:
    """This class defines a square.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        area(self): Calculates and returns the area of the square.
        __eq__(self, other): Checks if two squares are equal in area.
        __ne__(self, other): Checks if two squares are not equal in area.
        __lt__(self, other): Checks if one square has a smaller area than another.
        __le__(self, other): Checks if one square has a smaller or equal area than another.
        __gt__(self, other): Checks if one square has a larger area than another.
        __ge__(self, other): Checks if one square has a larger or equal area than another.

    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is a negative number.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is a negative number.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the squares have equal area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square has a smaller area than another.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the first square has a smaller area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square has a smaller or equal area than another.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the first square has a smaller or equal area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square has a larger area than another.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the first square has a larger area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square has a larger or equal area than another.

        Args:
            other (Square): The other Square object for comparison.

        Returns:
            bool: True if the first square has a larger or equal area, False otherwise.
        """
        return self.area() >= other.area()
