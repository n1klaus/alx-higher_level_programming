#!/usr/bin/python3
""" Module to check class Inheritance """


def is_kind_of_class(obj, a_class):
    """ Function to confirm if an object is a subclass of a class

    Args:
        obj: a python object
        a_class: a python class

    Returns:
        bool: True if the object is a subclass of the class
        otherwise False

    """
    return isinstance(obj, a_class)
