#!/usr/bin/python3

"""Module to test the Base model

"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Class Test Base

    """

    def test_base(self):
        """Function to test base
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base("Mahmoud")
        self.assertEqual(b6.id, "Mahmoud")

    def test_to_json_string(self):
        """Function to test to_json_string
        """
        r1 = Rectangle(10, 7, 2, 8, 50)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        res = "{'id': 50, 'width': 10, 'height': 7, 'x': 2, 'y': 8}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(dictionary)
        self.assertEqual(str_out.getvalue(), res)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(dictionary))
        self.assertEqual(str_out.getvalue(), res)

        res = '[{"id": 50, "width": 10, "height": 7, "x": 2, "y": 8}]\n'
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
        self.assertEqual(str_out.getvalue(), res)

        res = "<class 'str'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(json_dictionary))
        self.assertEqual(str_out.getvalue(), res)

    def test_save_to_file(self):
        """Function to test save_to_file
        """
        r1 = Rectangle(10, 7, 2, 8, 51)
        r2 = Rectangle(2, 4, 0, 0, 52)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            res = '[{"id": 51, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 52, "width": 2, "height": 4, "x": 0, "y": 0}]\n'
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
            self.assertEqual(str_out.getvalue(), res)

    def test_from_json_string(self):
        """Function to test from_json_string
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        res = "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, \
{'id': 7, 'width': 1, 'height': 7}]\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print("[{}] {}".format(type(list_input), list_input))
        self.assertEqual(str_out.getvalue(), res)

        res = '[<class \'str\'>] [{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}]\n'
        with patch('sys.stdout', new=StringIO()) as str_out:
            print("[{}] {}".format(type(json_list_input), json_list_input))
        self.assertEqual(str_out.getvalue(), res)

        res = "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, \
{'id': 7, 'width': 1, 'height': 7}]\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print("[{}] {}".format(type(list_output), list_output))
        self.assertEqual(str_out.getvalue(), res)

    def test_create(self):
        """Function to test create
        """
        r1 = Rectangle(3, 5, 1, 0, 55)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        res = '[Rectangle] (55) 1/0 - 3/5\n'
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
        self.assertEqual(str_out.getvalue(), res)

        res = '[Rectangle] (55) 1/0 - 3/5\n'
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
        self.assertEqual(str_out.getvalue(), res)

        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
