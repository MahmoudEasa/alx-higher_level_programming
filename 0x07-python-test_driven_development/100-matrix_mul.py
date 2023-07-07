#!/usr/bin/python3

"""Module to multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Function to multiplies 2 matrices

        Args:
            m_a (list): first list
            m_b (list): second list
    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if all(type(row) != list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if all(type(row) != list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(((type(ele) == int) or (type(ele) == float)) for ele in
       [num for row in m_a for num in row]):
        raise TypeError("m_a should contain\
 only integers or floats")

    if not all(((type(ele) == int) or (type(ele) == float))
       for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain\
 only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_a_size = len(m_a[0])
    row_b_size = len(m_b[0])
    m_a_len = len(m_a)
    m_b_len = len(m_b)

    a_b = []
    for i in range(m_a_len):
        a_b.append([0] * len(m_b[0]))
        for k in range(m_b_len):
            for j in range(len(m_b[k])):
                a_b[i][j] += (m_a[i][k] * m_b[k][j])

    return (a_b)
