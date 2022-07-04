#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """My c characters removing function

    Args:
        my_string: string

    Returns:
        new string without characters c or C
    """
    for row in matrix:
        for column in range(len(row)):
            if column is not len(row) - 1:
                print("{}".format(row[column]), end=" ")
            else:
                print("{}".format(row[column]), end="")
        print("".format())
