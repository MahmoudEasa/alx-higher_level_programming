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
        res = "[Square] (22) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.area(), 25)

        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), res)

        r1 = Square(2, 2)
        res = "[Square] (23) 2/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.area(), 4)

        res = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
        self.assertEqual(str_out.getvalue(), res)

        r1 = Square(3, 1, 3)
        res = "[Square] (24) 1/3 - 3\n"
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

        with self.assertRaises(TypeError):
            r = Square(5)
            r.size = "9"

    def test_square_area(self):
        """Test square area
        """
        r1 = Square(5)
        self.assertEqual(r1.area(), 25)
        r2 = Square(2, 2)
        self.assertEqual(r2.area(), 4)
        r3 = Square(3, 1, 3)
        self.assertEqual(r3.area(), 9)

    def test_square_size(self):
        """Test Square Size
        """
        s1 = Square(5)
        res = "[Square] (32) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(s1.size, 5)

        s1.size = 10
        res = "[Square] (32) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

    def test_square_update(self):
        """Test Square update
        """
        s1 = Square(5)
        res = "[Square] (35) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(10)
        res = "[Square] (10) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(1, 2)
        res = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(1, 2, 3)
        res = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(1, 2, 3, 4)
        res = "[Square] (1) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(x=12)
        res = "[Square] (1) 12/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(size=7, y=1)
        res = "[Square] (1) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1.update(size=7, id=89, y=1)
        res = "[Square] (89) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

    def test_square_to_dictionary(self):
        """Test Square to_dictionary
        """
        s1 = Square(10, 2, 1)
        res = "[Square] (33) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
        self.assertEqual(str_out.getvalue(), res)

        s1_dictionary = s1.to_dictionary()
        res = "{'id': 33, 'size': 10, 'x': 2, 'y': 1}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1_dictionary)
        self.assertEqual(str_out.getvalue(), res)
        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary))
        self.assertEqual(str_out.getvalue(), res)

        s2 = Square(1, 1)
        res = "[Square] (34) 1/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
        self.assertEqual(str_out.getvalue(), res)

        s2.update(**s1_dictionary)
        res = "[Square] (33) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
        self.assertEqual(str_out.getvalue(), res)

        self.assertFalse(s1 == s2)
