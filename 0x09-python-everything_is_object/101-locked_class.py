#!/usr/bin/python3
class LockedClass:
    """
    A class that locks down attribute assignments.

    This class is designed to only allow the creation of the 'first_name' attribute.
    Any attempt to set any other attribute will raise an AttributeError.
    """

    __slots__ = ['first_name']

