#!/usr/bin/python3
""" Module to define a depth first backtracking solution class """


from sys import argv, exit
class Queens():
    """ Class definition for solving an N queens puzzle on
    a NxN chessboard

    Attributes:
        __size (int): number of rows in the chessboard
    """

    def __init__(self):
        """ The constructor to initialize new permutations

        Args:
            argv (int): arguments array
        """
        if len(argv) != 2:
            print("Usage: nqueens N".format())
            exit(1)
        if argv[1].isdigit():
            if int(argv[1]) >= 4:
                self.__size = int(argv[1])
            else:
                print("N must be at least 4".format())
                exit(1)
        else:
            print("N must be a number".format())
            exit(1)

    def rows(self):
        """ Method to return the position of the queen on all the rows """
        rows = []
        complete_rows = []
        if self.__size % 4 != 2 or self.__size % 4 != 3:
            for index in range(self.__size):
                if index % 2 == 0:
                    rows.append(index)
        else:
            even_row = []
            odd_row = []
            for index in range(self.__size):
                if index % 2 == 0:
                    even_row.append(index)
                if index % 2 != 0:
                    odd_row.append(index)
            if self.__size % 4 == 2:
                odd_row.remove(1)
                odd_row.remove(3)
                odd_row.insert(0, 1)
                odd_row.insert(0, 3)
                odd_row.remove(5)
                odd_row.append(5)
                rows = even_row + odd_row
            if self.__size % 4 == 3:
                even_row.remove(2)
                even_row.append(2)
                odd_row.remove(1)
                odd_row.remove(3)
                odd_row.append(1)
                odd_row.append(3)
                rows = even_row + odd_row
        for row_index in range(self.__size):
            if rows[row_index]:
                complete_rows.append([row_index, rows[row_index]])
        return complete_rows

    def print_row(self):
        """ Method to print a permuatation for the chessboard of given size """
        print("{}".format(self.rows()))

if __name__ == "__main__":
    q = Queens()
    q.print_row()
