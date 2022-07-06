#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function to adds up all unique integers in a list

    Args:
        my_list: list of elements

    Returns:
        total sum of all unique integers
    """
    total = 0
    new_list = list(set(my_list))
    for elem in range(len(new_list)):
        total += new_list[elem]
    return total
