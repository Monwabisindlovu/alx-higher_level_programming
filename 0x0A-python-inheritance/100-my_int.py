#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int. This class includes
methods to invert the == and != operators. This class does not require any
modules to be imported.
"""

class MyInt(int):
    """
    A class that inherits from int and inverts the == and != operators.
    """
    
    def __eq__(self, other):
        """
        Inverts the == operator.
        
        Args:
            other: The object to be compared with.
            
        Returns:
            True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)
    
    def __ne__(self, other):
        """
        Inverts the != operator.
        
        Args:
            other: The object to be compared with.
            
        Returns:
            True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
