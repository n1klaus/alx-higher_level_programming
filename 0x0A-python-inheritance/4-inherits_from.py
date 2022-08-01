#!/usr/bin/python3
""" Module to check class Inheritance """


def inherits_from(obj, a_class):
    """ Function to confirm if an object is an instance of a class that
    inherited directly or indirectly from the specified class

    Args:
        obj: a python object
        a_class: a python class

    Returns:
        bool: True if the object is an instance of the class
        otherwise False

    """
    return type(obj) != a_class and isinstance(obj, a_class)
