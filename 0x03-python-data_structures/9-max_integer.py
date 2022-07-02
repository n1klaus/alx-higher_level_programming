#!/usr/bin/python3
def max_integer(my_list=[]):
    """My largest number in list printing function

    Args:
        my_list: list of integers

    Returns:
        largest integer in the list
    """
    my_list.sorted()
    return my_list[-1]
