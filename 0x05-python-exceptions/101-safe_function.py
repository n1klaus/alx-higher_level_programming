#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function to execute a function safely.

    Args:
        fct: pointer to a function
        args: list of arguments

    Returns:
        result of the function
        Otherwise None and prints the error in stderr
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
