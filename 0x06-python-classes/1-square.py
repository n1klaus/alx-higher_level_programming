#!/usr/bin/python3
""" Module to define a square class """


class Square():
    """Class definition for a square of given size

    Attributes:
        __size: size of the length

    """

    def __init__(self, size):
        """ The constructor to initialize new square objects

        Args:
            size: size of the length

        """
        self.__size = size

    @property
    def _size(self):
        """Getter method to retrieve private attributes of the instance

        Returns:
            size of the length of the instance

        """
        return self.__size

    @_size.setter
    def _size(self, size):
        """Setter method to change private attributes of the instance.

        Args:
            size: size of the length of the new instance

        Returns:
            size of the length of the instance.

        """
        self.__size = size
