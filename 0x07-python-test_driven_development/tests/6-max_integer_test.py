#!/usr/bin/python3

import unittest

"""Unittest for max_integer([..])
"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest for max_integer([..])
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)
        self.assertEqual(max_integer([4, 3, -1, 2]), 4)
        self.assertEqual(max_integer([-4, -3, -1, -2]), -1)
        self.assertEqual(max_integer([4]), 16)
        self.assertEqual(max_integer([]), 1)


if __name__ == '__main__':
    unittest.main()
