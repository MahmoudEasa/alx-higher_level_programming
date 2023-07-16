#!/usr/bin/python3

"""Module to test Rectangle model

"""
import unittest
from io import StringIO
from unittest.mock import patch
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

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_rectangle_display(self):
        r1 = Rectangle(4, 6)
        output = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), output)

        r2 = Rectangle(2, 2)
        output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r2.display()
        self.assertEqual(str_out.getvalue(), output)

    def test_rectangle_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        output = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), output)

        r2 = Rectangle(5, 5, 1, 0, 33)
        output = "[Rectangle] (33) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
        self.assertEqual(str_out.getvalue(), output)

    def test_rectangle_display2(self):
        r1 = Rectangle(2, 3, 2, 2)
        output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), output)

        r2 = Rectangle(3, 2, 1, 0)
        output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r2.display()
        self.assertEqual(str_out.getvalue(), output)


if __name__ == '__main__':
    unittest.main()
