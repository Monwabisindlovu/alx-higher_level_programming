#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.

    This function takes an integer `size` as input and prints a square of that size using the character '#'.
    If `size` is not an integer or if it is less than 0, the function raises an exception.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
