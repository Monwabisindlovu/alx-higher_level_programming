#!/usr/bin/python3
"""
This module contains a function is_same_class that returns True if the object is
exactly an instance of the specified class; otherwise False. This function does
not require any modules to be imported.
"""

def is_same_class(obj, a_class):
    """
    Function to check if an object is exactly an instance of a class.
    
    Args:
        obj: The object to be checked.
        a_class: The class to be compared with.
        
    Returns:
        True if the object is exactly an instance of the class, False otherwise.
    """
    return type(obj) is a_class
