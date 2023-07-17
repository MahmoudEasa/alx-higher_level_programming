#!/usr/bin/python3

"""Module to test Square model

"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class Test Square

    """

    def test_square(self):
        """Test square
        """
        r1 = Square(5)
        res = "[Square] (20) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.area(), 25)

        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), res)

        r1 = Square(2, 2)
        res = "[Square] (21) 2/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.area(), 4)

        res = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), res)

        r1 = Square(3, 1, 3)
        res = "[Square] (22) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.area(), 9)

        res = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), res)

        r2 = Square(2, 10, 0, 6)
        self.assertEqual(r2.id, 6)
        r3 = Square(10, 2, 0, 7)
        self.assertEqual(r3.id, 7)
        r4 = Square(10, 2, 0, 12)
        self.assertEqual(r4.id, 12)
        r5 = Square(2, 10, 0, 8)
        self.assertEqual(r5.id, 8)
        r6 = Square(2, 10, 0, "Mahmoud")
        self.assertEqual(r6.id, "Mahmoud")

    def test_square_err(self):
        """Test square errors
        """
        with self.assertRaises(TypeError):
            Square(10, "2")

        with self.assertRaises(ValueError):
            r = Square(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Square(10, 2)
            r.x = {}

    def test_square_area(self):
        """Test square area
        """
        r1 = Square(5)
        self.assertEqual(r1.area(), 25)
        r2 = Square(2, 2)
        self.assertEqual(r2.area(), 4)
        r3 = Square(3, 1, 3)
        self.assertEqual(r3.area(), 9)
