#!/usr/bin/python3

def copy_list(l):
    """
    Create and return a copy of a given list.

    Args:
        l (list): The list to be copied.

    Returns:
        list: A new list containing the same elements as the input list.

    Example:
        >>> my_list = [1, 2, 3]
        >>> new_list = copy_list(my_list)
        >>> print(new_list)
        [1, 2, 3]
    """
    return l[:]

