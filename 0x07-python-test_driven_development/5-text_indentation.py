#!/usr/bin/python3
"""Defines a text-printing function."""

def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, f"{char}\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]))

