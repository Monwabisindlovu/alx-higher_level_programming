#!/usr/bin/python3
"""
This module contains a class BaseGeometry. This class includes a method to
calculate the area of a shape, but this method is not yet implemented. This
class also includes a method to validate the value of an integer. This
class does not require any modules to be imported.
"""

class BaseGeometry:
    """
    A class that represents the base of geometry.
    
    Methods:
        area: Raises an Exception indicating that it's not implemented.
        integer_validator: Validates the value of an integer.
    """
    
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        
        Returns:
            None
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the value of an integer.
        
        Args:
            name: A string representing the name of the integer.
            value: An integer to be validated.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
            
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
