#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function to return a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: a dictionary of key and value pairs

    Returns:
        new dictionary with updated values
    """
    new_dictionary = {}
    for k in a_dictionary.keys():
        new_dictionary[k] = a_dictionary.get(k) * 2
    return new_dictionary
