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
            assert(id > 0)
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
        assert(isinstance(list_dictionaries, list))
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of a python object into a file

        Args:
            list_objs (list): list of instances of the Base class

        """
        assert(isinstance(list_objs, list))
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

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set from a dictionary

        Args:
            dictionary: double pointer to a dictionary of attributes

        Return:
            A newly created instance with attributes set

        """
        assert(isinstance(dictionary, dict))
        if cls.__name__ == 'Base':
            cls_object = cls()
        elif cls.__name__ == 'Rectangle':
            cls_object = cls(1, 1)
            cls_object.update(**dictionary)
        elif cls.__name__ == 'Square':
            cls_object = cls(1)
            cls_object.update(**dictionary)
        return cls_object

    @classmethod
    def load_from_file(cls):
        """ Loads a list of instance templates from a JSON file
            and creates an instance from the template

        Returns:
            list: a list of the created instances

        """
        fileName = cls.__name__ + ".json"
        json_list = list()
        instance_list = list()
        file_objs = str()
        dict_attr = dict()
        with open(fileName, mode="r", encoding="UTF-8") as o_file:
            file_objs = o_file.read()
        json_list.extend(cls.from_json_string(file_objs))
        for obj_attr in json_list:
            if cls.__name__ == 'Base':
                fake_obj = cls()
                dict_attr = fake_obj.__dict__
            else:
                if cls.__name__ == 'Rectangle':
                    fake_obj = cls(1, 1)
                elif cls.__name__ == 'Square':
                    fake_obj = cls(1)
                fake_obj.__dict__.clear()
                fake_obj.__dict__ = obj_attr
                dict_attr = fake_obj.to_dictionary()
            instance_list.append(cls.create(**dict_attr))
        return instance_list
