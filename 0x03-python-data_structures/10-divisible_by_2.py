#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """My multiples of 2 in list checking function

    Args:
        my_list: list of integers

    Returns:
        new list with boolean values with values
        True if integer is a multiple of 2
        False if integer is not a multiple of 2
    """
    checker = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            checker.append(True)
        else:
            checker.append(False)
    return checker
