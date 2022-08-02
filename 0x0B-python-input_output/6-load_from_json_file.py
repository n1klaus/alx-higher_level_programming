#!/usr/bin/python3
""" Module to operate on text file in JSON """


import json


def load_from_json_file(filename):
    """ Function to read an object from a JSON string in a text file

    Args:
        filename: name of the text file

    """
    with open(filename, "r", encoding="UTF-8") as o_file:
        json.load(o_file)
