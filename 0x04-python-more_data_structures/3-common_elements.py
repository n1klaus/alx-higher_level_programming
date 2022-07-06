#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Function to return a set of common elements in two sets

    Args:
        set_1: set 1 of elements
        set_2: set 2 of elements

    Returns:
        set of common elemnts in both sets
    """
    new_list = []
    for elem in list(set_1):
        if elem in list(set_2):
            new_list.append(elem)
    return set(new_list)
