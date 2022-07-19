#!/usr/bin/python3
class Square():
    """Class definition for a square.

    Args:
        size: size of the length

    Attributes:
        __size: size of the length of the new instance

    """

    def __init__(self, size):
        self.__size = size

    @property
    def _size(self):
        """Getter method to retrieve private attributes of the instance.

        Args:
            None

        Returns:
            size of the length of the instance.

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
