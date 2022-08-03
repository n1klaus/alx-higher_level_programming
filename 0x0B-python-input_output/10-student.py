#!/usr/bin/python3
""" Module to operate on class objects as JSON """


class Student:
    """ Class definition for Student

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

    def to_json(self, attrs=None):
        """ Method to list a class instance object attributes
        for JSON serialization

        Args:
            attrs (list): a list of attributes to select from

        Returns:
            a dictionary description

        """
        if attrs:
            dic = {}
            for item in attrs:
                dic.update({item: self.__dict__.get(item)})
            return dic
        return self.__dict__
