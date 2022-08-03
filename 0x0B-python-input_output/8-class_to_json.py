#!/usr/bin/python3
""" Module to operate on JSON """


def class_to_json(obj):
    """ Function to list a class instance object attributes
    for JSON serialization

    Args:
        obj: class instance object

    Returns:
        a dictionary description

    """
    return obj.__dict__
