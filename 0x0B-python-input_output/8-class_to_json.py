#!/usr/bin/python3
"""
This module contains a function that converts an object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the serializable attributes of the object.
    """
    serializable_attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value
    return serializable_attributes
