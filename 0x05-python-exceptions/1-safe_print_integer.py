#!/usr/bin/python3
def safe_print_integer(value):
    """Function to print an integer with "{:d}".format().

    Args:
        value: element to print

    Returns:
        True if value has been correctly printed
        Otherwise returns False
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except Exception as e:
        raise
    else:
        return False
