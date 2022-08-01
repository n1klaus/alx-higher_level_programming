#!/usr/bin/python3
""" Module to print object's data and behaviour """


def lookup(obj):
    """ Function to print a python object's attributes and methods

    Args:
        obj: a python object

    Returns:
        list: The list of available methods and attributes of the object
    """
    return dir(obj)
