#!/usr/bin/python3
def number_keys(a_dictionary):
    """Function to return the number of keys in a dictionary

    Args:
        a_dictionary: a dictionary of key and value pairs

    Returns:
        number of keys in the dictionary
    """
    key_list = a_dictionary.keys()
    return len(key_list)
