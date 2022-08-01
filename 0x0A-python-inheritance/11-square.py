#!/usr/bin/python3
""" Module to define Square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class definition for a square geometry shape

    Attributes:
        __size (int): size of the length of the square

    """

    def __init__(self, size):
        """ Constructor for initializing square instances

        Args:
            width (int): size of the length of the square

        """
        self.__size = self.integer_validator('size', size)

    def area(self):
        """ Method to calculate area of the square

        Returns:
            int: The calculated area of the square

        """
        return self.__size ** 2

    def __str__(self):
        """
        Method to provide unofficial string representation of the object
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
