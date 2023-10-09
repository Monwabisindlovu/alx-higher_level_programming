#!/usr/bin/python3
"""
This module contains a function lookup that returns the list of available
attributes and methods of an object. This function does not require any
modules to be imported.
"""

def lookup(obj):
    """
    Function to return the list of available attributes and methods of an object.
    
    Args:
        obj: The object whose attributes and methods are to be returned.
        
    Returns:
        A list of the attributes and methods of the object.
    """
    return dir(obj)
