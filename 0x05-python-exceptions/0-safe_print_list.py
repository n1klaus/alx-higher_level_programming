#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function to print x elements of a list.

    Args:
        my_list: list of elements
        x: number of elements to print

    Returns:
        Real number of elements printed
    """
    try:
        if x in range(my_list.__len__()):
            return x
    except Exception as e:
        raise
    else:
        return my_list.__len__()
    finally:
        for idx in range(my_list.__len__()):
            if idx < x:
                print("{}".format(my_list[idx]), end="")
        print()
