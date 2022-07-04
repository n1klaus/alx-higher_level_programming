#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """My matrix printing function

    Args:
        matrix: 2 dimensional array

    Returns:
        integer in matrix
    """
    for row in matrix:
        for column in range(len(row)):
            if column is not len(row) - 1:
                print("{:d}".format(row[column]), end=" ")
            else:
                print("{:d}".format(row[column]), end="")
        print("".format())
