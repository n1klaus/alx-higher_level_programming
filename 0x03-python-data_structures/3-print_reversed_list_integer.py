#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """My list elements reverse printing function

    Args:
        my_list: list of integers

    Returns:
        list in reverse
    """
    my_list.reverse()
    [print("{}".format(my_list[item])) for item in range(len(my_list))]
