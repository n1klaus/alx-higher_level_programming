#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """My c characters removing function

    Args:
        my_string: string

    Returns:
        new string without characters c or C
    """
    for row in matrix:
        for column in row:
            if column is not len(row):
                print("{}".format(column), end=" ")
            else:
                print("{}".format(column), end="")
        print("".format())
