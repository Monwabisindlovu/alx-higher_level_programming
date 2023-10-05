#!/usr/bin/python3
Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

Returns:
    numpy.ndarray: The product of m_a and m_b.

Raises:
    TypeError: If m_a or m_b is not a list, not a list of lists, contains non-numerical elements, or has rows of different sizes.
    ValueError: If m_a or m_b is empty or if their dimensions are incompatible for multiplication.
"""
"" Convert the matrices to numpy arrays """
try:
    a = np.array(m_a)
    b = np.array(m_b)
except Exception:
    raise TypeError("m_a and m_b must be a list of lists")

""" Check if the arrays are valid """
if a.size == 0 or b.size == 0:
    raise ValueError("m_a and m_b can't be empty")
if not (a.dtype == int or a.dtype == float) or not (b.dtype == int or b.dtype == float):
    raise TypeError("m_a and m_b should contain only integers or floats")
if len(a.shape) != 2 or len(b.shape) != 2:
    raise TypeError("m_a and m_b must be two-dimensional")
if not all(len(row) == len(a[0]) for row in a) or not all(len(row) == len(b[0]) for row in b):
    raise TypeError("each row of m_a and m_b must be of the same size")

""" Check if the arrays can be multiplied """
if a.shape[1] != b.shape[0]:
    raise ValueError("m_a and m_b can't be multiplied")

""" Perform the multiplication and return the result """
return np.matmul(a, b)

