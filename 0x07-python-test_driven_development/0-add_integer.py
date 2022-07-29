#!/usr/bin/python3
""" Module to define an adding function """


def add_integer(a, b=98):
    """Function to add two numbers and return the result

    Args:
        a ('int'): first variable
        b ('int', optional): second variable

    Returns:
        int: the result of the addition

    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            sum = int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
    return sum


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
