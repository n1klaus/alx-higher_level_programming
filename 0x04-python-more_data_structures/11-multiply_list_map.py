#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Function to return a list with all values multiplied by a number
    without using any loops.

    Args:
        my_list: a list of elements
        number: integer value

    Returns:
        new list with calculated values
    """
    return (new_list := list(map((lambda x: x * number), my_list)))
