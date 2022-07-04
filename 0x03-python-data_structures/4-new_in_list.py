#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """My copied list elements replacing function

    Args:
        my_list: list of integers
        idx: index of elements
        element: new element

    Returns:
        list with replaced element if True
        old list if False
    """
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
