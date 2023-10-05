#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if they contain non-integer/float elements,
                   or if rows have different sizes.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    """ Check if all rows have the same length in m_a and m_b """
    len_a = len(m_a[0]) if m_a else 0
    len_b = len(m_b[0]) if m_b else 0

    if not all(len(row) == len_a for row in m_a) or not all(len(row) == len_b for row in m_b):
        raise ValueError("each row of m_a must be of the same size and each row of m_b must be of the same size")

    if len_a != len_b:
        raise ValueError("m_a and m_b can't be multiplied")

    """ Check if elements are integers or floats """
    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    """ Perform matrix multiplication """
    result = [[0 for _ in range(len_b)] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len_b):
            for k in range(len_b):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

