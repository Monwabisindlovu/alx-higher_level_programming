#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        ValueError: If m_a or m_b is empty or has different-sized rows.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j]
            row.append(product)
        result.append(row)

    return result
