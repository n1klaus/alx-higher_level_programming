#!/usr/bin/python3
""" Module to represent a pascal's triangle """


def pascal_triangle(n):
    """ Function to represent pascal's triangle

    Args:
        n (int): integer number

    Return:
        a list of lists of integers representing the Pascal's triangle of n

    """
    inner_list = []
    full_matrix = []
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        return inner_list
    for row in range(n):
        for column in range(row + 1):
            if column == 0 or column == row:
                inner_list.append(1)
            else:
                inner_list.append(full_matrix[row - 1][column] +
                                  full_matrix[row - 1][column - 1])
        full_matrix.append(inner_list.copy())
        inner_list.clear()
    return full_matrix
