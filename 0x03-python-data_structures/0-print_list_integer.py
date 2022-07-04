#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """My List printing function

    Args:
        my_list: list of integers

    Returns:
        list item
    """
    [print("{:d}".format(my_list[index])) for index in range(len(my_list))]
