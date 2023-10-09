#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list. This class includes
a method to print the list in ascending order. This class does not require any
modules to be imported.
"""

class MyList(list):
    """
    A class that inherits from list.
    
    Methods:
        print_sorted: Prints the list in ascending order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
