#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
        TypeError: If the matrices contain invalid data, e.g., non-numeric elements.

    Returns:
        list of lists: The result of matrix multiplication as a list of lists.

    Example:

    >>> m_a = [[1, 2], [3, 4]]
    >>> m_b = [[1, 2], [3, 4]]
    >>> result = lazy_matrix_mul(m_a, m_b)
    >>> print(result)
    [[ 7 10]
     [15 22]]
    """
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.matmul(np_m_a, np_m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("Matrices cannot be multiplied due to incompatible dimensions")
    except TypeError:
        raise TypeError("Matrices must contain only integers or floats")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

