#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """My list element replacing function

    Args:
        my_list: list of integers
        idx: index of element
        element: element to insert

    Returns:
        new list with element at the index if True
        old list if False
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
