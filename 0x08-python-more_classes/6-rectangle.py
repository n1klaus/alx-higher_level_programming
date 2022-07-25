#!/usr/bin/python3
""" Module to define a rectangle class """


class Rectangle():
    """ Class definition for a rectangle

    Attributes:
        __width (int): widht of the rectangle
        __height (int): height of the rectangle
    """
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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
        try:
            if isinstance(height, int) and height >= 0:
                self.__height = int(height)
        except ValueError:
            print("height must be >= 0".format())
        except TypeError:
            print("height must be an integer".format())
        except Exception:
            raise

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

    def __str__(self):
        """ Print # characters for the size of the rectangle """
        for h in range(self.__height):
            for w in range(self.__width):
                print("#".format(w), end="")
            if h != self.__height - 1:
                print("".format(h))
        return "".format()

    def __repr__(self):
        """ Print the command representation of creating
        a similar rectangle instance """
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of the class is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...".format())
