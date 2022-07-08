#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function to return a set of all distinct elements

    Args:
        set_1: set 1 of elements
        set_2: set 2 of elements

    Returns:
        set of distinct elements in both sets
    """
    return set(set_1 ^ set_2)
