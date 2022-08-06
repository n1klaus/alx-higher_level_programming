#!/usr/bin/python3
""" Module for class Base """


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
