#!/usr/bin/python3

import numpy as np

"""Module to multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """Function to multiplies 2 matrices by using the module NumPy
    """
    result = np.dot(m_a, m_b)

    return (result)
