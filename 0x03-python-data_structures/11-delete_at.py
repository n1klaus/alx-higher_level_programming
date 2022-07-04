#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """My index in list deleting function

    Args:
        my_list: list of integers
        idx: index

    Returns:
        list with removed index or
        unchanged list if range is invalid
    """
    if idx > 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
