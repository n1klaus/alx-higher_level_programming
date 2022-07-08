#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function to returns the weighted average of all integers
    tuple (<score>, <weight>)

    Args:
        my_list: a list of elements

    Returns:
        weightd average score or
        0 if list is empty
    """
    if my_list:
        scores = 0
        weights = 0
        avg = 0
        for tup in my_list:
            scores += (tup[0] * tup[1])
            weights += tup[1]
        avg = (scores / weights)
        return avg
    else:
        return (0)
