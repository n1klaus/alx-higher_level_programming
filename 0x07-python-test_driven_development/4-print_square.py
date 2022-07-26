#!/usr/bin/python3
""" Module to define a square printing function using # characters """


def print_square(size):
    """Function to print a square using # characters

    Args:
        size ('int'): length of the square

    """
    if isinstance(size, int) and not isinstance(size, float):
        if size >= 0:
            for len in range(size):
                for height in range(size):
                    if height != size - 1:
                        print("#".format(height), end="")
                    else:
                        print("#".format())
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
