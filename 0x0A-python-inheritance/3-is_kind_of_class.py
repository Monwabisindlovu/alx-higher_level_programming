#!/usr/bin/python3
"""
This module contains a function is_kind_of_class that returns True if the object is
an instance of, or if the object is an instance of a class that inherited from, the
specified class; otherwise False. This function does not require any modules to be imported.
"""

def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.
    
    Args:
        obj: The object to be checked.
        a_class: The class to be compared with.
        
    Returns:
        True if the object is an instance of, or if the object is an instance of a class
        that inherited from, the specified class; False otherwise.
    """
    return isinstance(obj, a_class)
