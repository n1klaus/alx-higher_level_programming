#!/usr/bin/python3
""" Module to define a square class """


class Square():
    """Class definition for a square of given size

    Attributes:
        __size (int): size of the length

    """

    def __init__(self, size=0):
        """ The constructor to initialize new square objects

        Args:
            size (:obj:'int'): size of the length

        """
        try:
            if size >= 0 and isinstance(size, int):
                self.__size = size
        except TypeError:
            print("size must be an integer".format())
        except ValueError:
            print("size must be >= 0".format())
        except Exception:
            raise

    def area(self):
        """Method to calculate the area of the square

        Returns:
            int: area of the square for the instance

        """
        return self.__size ** 2
