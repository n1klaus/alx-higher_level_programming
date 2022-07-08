#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function to compute the square value of all integers of a matrix

    Args:
        matrix: 2 dimensional array

    Returns:
        new matrix with the computed values
    """
    new_matrix = []
    new_row = []
    for row in matrix:
        for column in row:
            new_row.append(column * column)
        arow = new_row[:]
        new_row.clear()
        new_matrix.append(arow)
    return new_matrix
