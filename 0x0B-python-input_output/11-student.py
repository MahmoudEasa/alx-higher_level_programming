#!/usr/bin/python3
"""Module to Write a class Student that defines a student
"""


class Student:
    """Class Student

        Attributes:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to retrieves a dictionary representation
            of a Student instance

            Args:
                arrts (list): list of keys
        """
        student = {}
        if type(attrs) == list:
            for arg in attrs:
                if arg in list(self.__dict__.keys()):
                    student[arg] = self.__dict__[arg]
        else:
            student = {
                        'first_name': self.first_name,
                        'last_name': self.last_name,
                        'age': self.age
                    }
        return (student)

    def reload_from_json(self, json):
        """Function to replaces all attributes of the Student instance

            Args:
                json (dict): The dectionary
        """

        if type(json) == dict:
            for key in list(json.keys()):
                if key[0:2] != "__" and key in list(self.__dict__.keys()):
                    self.__dict__[key] = json[key]
