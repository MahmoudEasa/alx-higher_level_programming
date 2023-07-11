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
