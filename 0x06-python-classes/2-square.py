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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
