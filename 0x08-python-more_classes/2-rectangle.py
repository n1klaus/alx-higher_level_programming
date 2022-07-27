#!/usr/bin/python3
""" Module to define a rectangle class """


class Rectangle():
    """ Class definition for a rectangle

    Attributes:
        width (int): widht of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """ The constructor to initialize new rectangle instances

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the Rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter method to retrieve instance width attribute

        Returns:
            int: width of the rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter method to change instance width attribute

        Args:
            width (int): width of the retangle instance
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Getter method to retrieve height attribute

        Returns:
            int: height of the rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter method to change the height attribute

        Args:
            height (int): height of the rectangle instances
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Method to compute the area of the rectangle instance

        Returns:
            The area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Method to compute the perimeter of the rectangle instance

        Returns:
            The perimeter of the rectangle
        """
        perimeter = 0
        if self.__width != 0 or self.__height != 0:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter
