#!/usr/bin/python3
""" Module to add new object data """


def add_attribute(obj, name=None, value=None):
    """ Function to add new attributes to a python object

    Args:
        obj: a python object
        name: name of the attribute
        value: value of the attribute to be saved in object

    """
    if obj.__class__ in (tuple, str):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(name, value)
