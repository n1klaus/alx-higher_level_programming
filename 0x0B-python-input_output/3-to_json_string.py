#!/usr/bin/python3
""" Module to operate on JSON """


import json


def to_json_string(my_obj):
    """ Function to serialize an object into a JSON string

    Args:
        my_obj: object to dump as JSON

    Returns:
        the encoded object

    """
    try:
        return json.dumps(my_obj)
    except TypeError:
        raise
