#!/usr/bin/python3

def magic_string():
    """
    This function returns the string "BestSchool" repeated n times,
    where n is the number of times the function has been called.

    Returns:
        str: The string "BestSchool" repeated n times.
    """
    magic_string.counter = getattr(magic_string, 'counter', -1) + 1
    return "BestSchool, " * magic_string.counter + "BestSchool"

