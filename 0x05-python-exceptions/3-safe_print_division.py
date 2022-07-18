#!/usr/bin/python3
def safe_print_division(a, b):
    """Function to divides 2 integers and prints the result.

    Args:
        a: integer number
        b: integer number

    Returns:
        the value of the division, otherwise: None
    """
    c = None
    try:
        c = a / b
    except Exception as e:
        raise
    finally:
        print("Inside result: {}".format(c))
        return c
