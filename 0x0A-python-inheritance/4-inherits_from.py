#!/usr/bin/python3
"""
This module contains a function inherits_from that returns True if the object is
an instance of a class that inherited (directly or indirectly) from the specified
class; otherwise False. This function does not require any modules to be imported.
"""

def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    
    Args:
        obj: The object to be checked.
        a_class: The class to be compared with.
        
    Returns:
        True if the object is an instance of a class that inherited (directly or
        indirectly) from the specified class; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
