#!/usr/bin/python3
def max_integer(my_list=[]):
    """My largest number in list printing function

    Args:
        my_list: list of integers

    Returns:
        largest integer in the list
    """
    if len(my_list) > 0:
        my_list.sort()
        return my_list[-1]
    else:
        return None
