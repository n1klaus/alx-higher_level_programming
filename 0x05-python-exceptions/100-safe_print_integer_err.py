#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Function to print a value if it is an integer.

    Args:
        value: any type of value

    Returns:
        True if value is an integer, and prints it
        Otherwise False and prints error in stderr
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
