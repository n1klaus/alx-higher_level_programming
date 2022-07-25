#!/usr/bin/python3
""" Module to define a rectangle class """


class Rectangle():
    """ Class definition for a rectangle

    Attributes:
        __width (int): widht of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """ The constructor to initialize new rectangle instances

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the Rectangle
        """
        try:
            if isinstance(height, int) and height >= 0:
                self.__height = int(height)
        except ValueError:
            print("height must be >= 0".format())
        except TypeError:
            print("height must be an integer".format())
        except Exception:
            raise

        try:
            if isinstance(width, int) and width >= 0:
                self.__width = int(width)
        except ValueError:
            print("width must be >= 0".format())
        except TypeError:
            print("width must be an integer".format())
        except Exception:
            raise

    @property
    def _width(self):
        """ Getter method to retrieve instance width attribute

        Returns:
            int: width of the rectangle instance
        """
        return self.__width

    @_width.setter
    def _width(self, width):
        """ Setter method to change instance width attribute

        Args:
            width (int): width of the retangle instance
        """
        try:
            if isinstance(width, int) and width >= 0:
                self.__width = int(width)
        except ValueError:
            print("width must be >= 0".format())
        except TypeError:
            print("width must be an integer".format())
        except Exception:
            raise

    @property
    def _height(self):
        """ Getter method to retrieve height attribute

        Returns:
            int: height of the rectangle instance
        """
        return self.__height

    @_height.setter
    def _height(self, height):
        """ Setter method to change the height attribute

        Args:
            height (int): height of the rectangle instances
        """
        try:
            if isinstance(height, int) and height >= 0:
                self.__height = int(height)
        except ValueError:
            print("height must be >= 0".format())
        except TypeError:
            print("height must be an integer".format())
        except Exception:
            raise
