#!/usr/bin/python3

"""Module to multiplies 2 matrices by using the module NumPy



"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function to multiplies 2 matrices by using the module NumPy
    """

    return (np.matmul(m_a, m_b))
