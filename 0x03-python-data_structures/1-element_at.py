#!/usr/bin/python3
def element_at(my_list, idx):
    """My list element retrieving function

    Args:
        my_list: list of integers
        idx: index of element

    Returns:
        index of the list element if True
        None if False
    """
    return None if idx < 0 or idx > len(my_list) - 1 else my_list[idx]
