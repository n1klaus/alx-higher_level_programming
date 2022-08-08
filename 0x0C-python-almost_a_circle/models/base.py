#!/usr/bin/python3
""" Module for class Base """


import json


class Base:
    """ Class definition for Base objects

    Attributes:
        __nb_objects (int) : number of instances initialized by class
        id (int): id of the instance

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor to instantiate new class instances

        Args:
            id (int, optional): id of the instance

        """
        if id is not None:
            assert(isinstance(id, int))
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method to encode python object into JSON string

        Args:
            list_dictionaries ('list' of obj:'dict'): list of dictionaries

        Returns:
            JSON string representation of list_dictionaries

        """
        if list_dictionaries is None or not list_dictionaries:
            return str("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of a python object into a file

        Args:
            list_objs (list): list of instances of the Base class

        """
        my_filename = str(cls.__name__) + ".json"
        my_list = list()
        encoded_string = str()
        with open(my_filename, mode="w", encoding="UTF-8") as a_file:
            if list_objs is not None:
                for item in list_objs:
                    my_list.append(item.__dict__)
                encoded_string = cls.to_json_string(my_list)
            a_file.write(encoded_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list from a JSON string representation

        Args:
            json_string: a JSON string of list of dictionaries

        Returns:
            list: a list of the JSON string

        """
        if json_string is None or not json_string:
            return (list())
        return list(json.loads(json_string))
