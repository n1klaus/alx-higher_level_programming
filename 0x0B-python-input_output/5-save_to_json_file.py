#!/usr/bin/python3
""" Module to operate on text file in JSON """


import json


def save_to_json_file(my_obj, filename):
    """ Function to write an object from a JSON string to a text file

    Args:
        my_obj: object to dump to file
        filename: name of the text file

    Returns:
        the decoded object

    """
    with open(filename, "w", encoding="UTF-8") as o_file:
        json.dump(my_obj, o_file)
