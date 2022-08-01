#!/usr/bin/python3
""" Module to define Rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class definition for a rectangle geometry shape

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle

    """

    def __init__(self, width, height):
        """ Constructor for initializing rectangle instances

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        super().__init__()
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def area(self):
        """ Method to calculate area of the rectangle

        Returns:
            int: The calculated area of the rectangle

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method to provide unofficial string representation of the object
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                   self.__height)
