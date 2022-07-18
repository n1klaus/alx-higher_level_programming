#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function to prints the first x elements of a list and only integers

    Args:
        my_list: list of elements
        x: number of elements to print

    Returns:
        the real number of integers printed
    """
    try:
        c = 0
        for idx in range(x):
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]), end="")
                c += 1
        print()
        return c
    except Exception as e:
        raise
