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

    m_a_len = len(m_a)
    m_b_len = len(m_b)

    if m_a_len and type(m_a[0]) != list:
        raise TypeError("m_a must be a list of lists")
    if m_b_len and type(m_b[0]) != list:
        raise TypeError("m_b must be a list of lists")

    if m_a_len == 0:
        raise ValueError("m_a can't be empty")
    if m_b_len == 0:
        raise ValueError("m_b can't be empty")

    row_a_size = len(m_a[0])
    row_b_size = len(m_b[0])

    a_b = []
    for i in range(m_a_len):
        m_a_i_len = len(m_a[i])
        m_b_i_len = len(m_b[i])

        if m_a_i_len == 0:
            raise ValueError("m_a can't be empty")
        if m_b_i_len == 0:
            raise ValueError("m_b can't be empty")

        a_b.append([0] * m_a_i_len)
        for k in range(row_b_size):
            for j in range(m_a_i_len):
                m_b_j_len = len(m_b[j])
                if (type(m_a[i][j]) not in [int, float]):
                    raise TypeError("m_a should contain\
 only integers or floats")
                if (type(m_b[i][j]) not in [int, float]):
                    raise TypeError("m_b should contain\
 only integers or floats")

                if m_a_i_len != row_a_size:
                    raise TypeError("each row of m_a must be of the same size")
                if m_b_j_len != row_b_size:
                    raise TypeError("each row of m_b must be of the same size")

                if m_a_i_len != m_b_len:
                    raise ValueError("m_a and m_b can't be multiplied")

                a_b[i][k] += (m_a[i][j] * m_b[j][k])

    return (a_b)
