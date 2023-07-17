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
        """Test rectangle
        """
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
        """Test rectangle errors
        """
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
        """Test rectangle area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_rectangle_display(self):
        """Test rectangle display
        """
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
        """Test rectangle str
        """
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
        """Test rectangle display
        """
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

    def test_rectangle_update(self):
        """Test rectangle update
        """
        r1 = Rectangle(10, 10, 10, 10)
        res = "[Rectangle] (21) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(89)
        res = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(89, 2)
        res = "[Rectangle] (89) 10/10 - 2/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(89, 2, 3)
        res = "[Rectangle] (89) 10/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(89, 2, 3, 4)
        res = "[Rectangle] (89) 4/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(89, 2, 3, 4, 5)
        res = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(height=1)
        res = "[Rectangle] (89) 4/5 - 2/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(width=1, x=2)
        res = "[Rectangle] (89) 2/5 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(y=1, width=2, x=3, id=89)
        res = "[Rectangle] (89) 3/1 - 2/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1.update(x=1, height=2, y=3, width=4)
        res = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_to_dictionary(self):
        """Test rectangle to_dictionary
        """
        r1 = Rectangle(10, 2, 1, 9)
        res = "[Rectangle] (19) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        res = "{'id': 19, 'width': 10, 'height': 2, 'x': 1, 'y': 9}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1_dictionary)
        self.assertEqual(str_out.getvalue(), res)
        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
        self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(1, 1)
        res = "[Rectangle] (20) 0/0 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
        self.assertEqual(str_out.getvalue(), res)

        r2.update(**r1_dictionary)
        res = "[Rectangle] (19) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
        self.assertEqual(str_out.getvalue(), res)

        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
