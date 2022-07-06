#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function to print a dictionary by ordered keys

    Args:
        a_dictionary: a dictionary of key and value pairs

    Returns:
        ordered dictionary by keys
    """
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary.get(k)))
