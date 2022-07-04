#!/usr/bin/python3
def no_c(my_string):
    """My c characters removing function

    Args:
        my_string: string

    Returns:
        new string without characters c or C
    """
    new_string = ""
    for char in range(len(my_string)):
        if my_string[char] not in "cC":
            new_string += (my_string[char])
    return new_string
