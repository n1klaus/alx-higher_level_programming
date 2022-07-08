#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Function to delete a key in a dictionary.

    Args:
        a_dictionary: a dictionary of key and value pairs
        key: key item

    Returns:
        dictionary with updated values
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
