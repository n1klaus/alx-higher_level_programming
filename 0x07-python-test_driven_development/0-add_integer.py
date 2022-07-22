#!/usr/bin/python3
""" Module to define an adding function """


def add_integer(a, b=98):
    """Function to add two numbers and return the result

    Args:
        a (:obj:'int'): first variable
        b (:obj:'int', optional): second variable

    Returns:
        int: the result of the addition

    """
    try:
        if isinstance(a, (int, float)):
            if isinstance(b, (int, float)):
                sum = int(a) + int(b)
            else:
                raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")
    except Exception as e:
        raise
    return sum


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
