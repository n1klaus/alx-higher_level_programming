#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Function to replace or add key/value in a dictionary.

    Args:
        a_dictionary: a dictionary of key and value pairs
        key: key item
        value: value from the key

    Returns:
        dictionary with updated values
    """
    a_dictionary[key] = value
    return a_dictionary
