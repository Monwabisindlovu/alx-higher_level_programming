#!/usr/bin/python3
#!/usr/bin/python3
"""
Module that defines a class with restricted attribute assignment.
"""

class LockedClass:
    """
    A class that only allows the creation of a 'first_name' attribute.

    This class is designed to restrict dynamic attribute creation, allowing only
    the 'first_name' attribute to be set. Any other attribute assignment will raise
    an AttributeError.
    """

    __slots__ = ['first_name']

