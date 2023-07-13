#!/usr/bin/python3

"""Module to test Rectangle model

"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class Test Rectangle

    """

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r3.id, 7)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.id, 12)
        r5 = Rectangle(2, 10, 0)
        self.assertEqual(r5.id, 8)
        r6 = Rectangle(2, 10, 0, 0, "Mahmoud")
        self.assertEqual(r6.id, "Mahmoud")

    def test_rectangle_err(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


if __name__ == '__main__':
    unittest.main()
