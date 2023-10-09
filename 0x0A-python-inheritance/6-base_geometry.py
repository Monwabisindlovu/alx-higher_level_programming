#!/usr/bin/python3
"""
This module contains a class BaseGeometry. This class includes a method to
calculate the area of a shape, but this method is not yet implemented. This
class does not require any modules to be imported.
"""

class BaseGeometry:
    """
    A class that represents the base of geometry.
    Methods:
        area: Raises an Exception indicating that it's not implemented.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
