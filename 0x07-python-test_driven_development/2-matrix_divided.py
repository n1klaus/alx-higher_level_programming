#!/usr/bin/python3
""" Module to define a matrix dividing function """


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix

    Args:
        matrix (:obj:list of lists of 'int' or 'float):
        a 2 dimensional list of lists
        div (:obj:'int' or 'float'): variable to divide the matrix elements

    Returns:
        new matrix with the new results

    """
    inner_list = []
    full_matrix = []
    matrixError = r"matrix must be a matrix (list of lists) of integers/floats"
    rowSizeError = r"Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, (list)) or\
            len(matrix) == 0 or\
            not isinstance(matrix[0], (list)) or\
            len(matrix[0]) == 0:
        raise TypeError(matrixError)
    for row in range(len(matrix)):
        if row is not len(matrix) - 1:
            if len(matrix[row]) != len(matrix[row + 1]):
                raise TypeError(rowSizeError)
        for column in matrix[row]:
            if isinstance(column, (int, float)):
                inner_list.append(round((column / div), 2))
            else:
                raise TypeError(matrixError)
        full_matrix.append(inner_list.copy())
        inner_list.clear()
    return full_matrix


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
