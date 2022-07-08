#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Function to delete keys with a specific value in a dictionary

    Args:
        a_dictionary: a list of key-value elements
        value: value to search

    Returns:
        dictionary without deleted key(s) or
        unchanged dictionary if value doesn't exist
    """
    for tup in list(a_dictionary.items()):
        if value is tup[1]:
           a_dictionary.pop(tup[0])
    return a_dictionary
