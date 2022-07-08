#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function to return a set of all distinct elements

    Args:
        set_1: set 1 of elements
        set_2: set 2 of elements

    Returns:
        set of distinct elements in both sets
    """
    new_list = []
    for elem in list(set_1):
        for item in list(set_2):
            if elem not in list(set_2):
                new_list.append(elem)
            if item not in list(set_1):
                new_list.append(item)
    return set(new_list)
