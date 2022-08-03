#!/usr/bin/python3
""" Module to operate on class objects as JSON """


class Student:
    """ Class definition for student

    Attributes:
        first_name: first name of the student
        last_name: last name of the student
        age: age of the student

    """
    def __init__(self, first_name, last_name, age):
        """ Constructor to initialize class instances

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method to list a class instance object attributes
        for JSON serialization

        Returns:
            a dictionary description

        """
        return self.__dict__
