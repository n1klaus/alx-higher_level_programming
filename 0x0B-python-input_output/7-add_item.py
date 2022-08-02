#!/usr/bin/python3
""" Module to operate on arguments in JSON """


import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def load_add_save(item=None):
    """ Function to load an object from a JSON string in the arguments,
        add the arguument to a list object and finally
        dump that object to a JSON file

    Args:
        item: JSON string item

    Returns:
        decoded object

    """
    my_list = []
    try:
        o_load = load_from_json_file("add_item.json")
        if o_load:
            my_list.extend(o_load)
    except Exception as e:
        pass

    if item:
        for i in item.split():
            my_list.append(i)

    try:
        save_to_json_file(my_list, "add_item.json")
    except Exception as e:
        raise


if __name__ == "__main__":
    if len(argv) == 1:
        load_add_save()
    else:
        ln = len(argv)
        s = ""
        for i in range(1, ln):
            s += argv[i] + " "
        s = s.strip()
        load_add_save(s)
