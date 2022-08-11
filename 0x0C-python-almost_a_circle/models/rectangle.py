#!/usr/bin/python3
""" Module for class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Class definition for Rectangle objects

    Attributes:
        width (int): base length of the rectangle
        height (int): height of the rectangle
        x (int: x coordinate position
        y (int): y coordinate position
        id (int): id of the instance

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to instantiate new class instances

        Args:
            width (int): base length of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate position
            y (int, optional): y coordinate position
            id (int, optional): id of the instance

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method to access width attribute

        Returns:
            int: base length of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method to modify width attribute

        Args:
            value (int): new value for width

        Raises:
            TypeError: if it is a Non-Integer values
            ValueError: if it is a Integer value less than or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method to access height attribute

        Returns:
            int: height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method to modify height attribute

        Args:
            value (int): new value for height

        Raises:
            TypeError: if it is a Non-Integer values
            ValueError: if it is a Integer value less than or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter method to access x coordinate attribute

        Returns:
            int: x coordinate position of the rectangle

        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method to modify x coordinate attribute

        Args:
            value (int): new value for x

        Raises:
            TypeError: if it is a Non-Integer values
            ValueError: if it is a Integer value less than 0

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter method to access y coordinate attribute

        Returns:
            int: y coordinate position of the rectangle

        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method to modify y coordinate attribute

        Args:
            value (int): new value for y

        Raises:
            TypeError: if it is a Non-Integer values
            ValueError: if it is a Integer value less than 0

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method to calculate the area of the rectangle

        Returns:
            int: area of the rectangle

        """
        return (self.__width * self.__height)

    def display(self):
        """ Method to print rectangle instance in stdout using # characters
            by using x and y coordiates as offsets

        """
        h_spaced = False
        w_spaced = False
        for h in range(self.__height):
            if h < self.__y and not h_spaced:
                for h_space in range(self.__y):
                    print(" ".format(h_space))
                h_spaced = True
            for w in range(self.__width):
                if w < self.__x and not w_spaced:
                    for w_space in range(self.__x):
                        print(" ".format(w_space), end="")
                    w_spaced = True
                if w == self.__width - 1:
                    print("#".format())
                else:
                    print("#".format(), end="")
            w_spaced = False

    def __str__(self):
        """ Method to override printable string representation of the instance

        Returns:
            str: printable string representation of instance

        """
        my_string = str()
        my_string += "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                      self.id,
                                                      self.__x,
                                                      self.__y,
                                                      self.__width,
                                                      self.__height)
        return my_string

    def update(self, *args, **kwargs):
        """ Method to assign from positional and key/value elements
            in argument list to each instance attributes

        """
        if args or kwargs:
            assert(all(isinstance(arg, int) for arg in args))
            assert(all(isinstance(kwarg, int) for kwarg in kwargs.values()))
            for index in range(max(len(args), len(kwargs))):
                if index == 0 or "id" in kwargs:
                    if index < len(args):
                        self.id = args[index]
                    elif kwargs.get("id"):
                        self.id = kwargs.get("id")
                if index == 1 or "width" in kwargs:
                    if index < len(args):
                        self.__width = args[index]
                    elif kwargs.get("width"):
                        self.__width = kwargs.get("width")
                if index == 2 or "height" in kwargs:
                    if index < len(args):
                        self.__height = args[index]
                    elif kwargs.get("height"):
                        self.__height = kwargs.get("height")
                if index == 3 or "x" in kwargs:
                    if index < len(args):
                        self.__x = args[index]
                    elif kwargs.get("x"):
                        self.__x = kwargs.get("x")
                if index == 4 or "y" in kwargs:
                    if index < len(args):
                        self.__y = args[index]
                    elif kwargs.get("y"):
                        self.__y = kwargs.get("y")

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle instance """
        d = dict()
        for key, value in self.__dict__.items():
            split_string = list(key.split("_"))
            d[split_string[-1]] = value
        return d
