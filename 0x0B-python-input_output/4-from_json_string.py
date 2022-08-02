#!/usr/bin/python3
""" Module to operate on JSON """


import json


def from_json_string(my_str):
    """ Function to deserialize an object from a JSON string

    Args:
        my_str: object to load from JSON

    Returns:
        the decoded object

    """
    try:
        return json.loads(my_str)
    except TypeError:
        raise
