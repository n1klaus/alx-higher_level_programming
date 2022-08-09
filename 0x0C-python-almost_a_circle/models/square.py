#!/usr/bin/python3
""" Module for class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class definition for Square objects """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor to instantiate new class instances

        Args:
            size (int): length of the size of the square
            x (int, optional): x coordinate position
            y (int, optional): y coordinate position
            id (int, optional): id of the instance

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method to access size attribute

        Returns:
            int: length of the size of the square

        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """ Setter method to modify size attribute

        Args:
            value (int): new value for the length of the size of the square

        Raises:
            TypeError: if it is a Non-Integer values
            ValueError: if it is a Integer value less than or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = self._Rectangle__height = value

    def __str__(self):
        """ Method to override printable string representation of the instance

        Returns:
            str: printable string representation of instance

        """
        my_string = str()
        my_string += "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                   self.id,
                                                   self._Rectangle__x,
                                                   self._Rectangle__y,
                                                   self._Rectangle__width)
        return my_string

    def update(self, *args, **kwargs):
        """ Method to assign from positional and key/value elements
            in argument list to each instance attributes

        """
        if args or kwargs:
            assert(all(isinstance(arg, int) for arg in args))
            assert(all(isinstance(kwarg, int) for kwarg in kwargs.values()))
            for index in range(max(len(args), len(kwargs))):
                if index == 0:
                    if index < len(args):
                        self.id = args[index]
                    elif kwargs.get("id"):
                        self.id = kwargs.get("id")
                if index == 1:
                    if index < len(args):
                        self._Rectangle__width = args[index]
                        self._Rectangle__height = args[index]
                    elif kwargs.get("size"):
                        self._Rectangle__width = kwargs.get("size")
                        self._Rectangle__height = kwargs.get("size")
                if index == 2:
                    if index < len(args):
                        self._Rectangle__x = args[index]
                    elif kwargs.get("x"):
                        self._Rectangle__x = kwargs.get("x")
                if index == 3:
                    if index < len(args):
                        self._Rectangle__y = args[index]
                    elif kwargs.get("y"):
                        self._Rectangle__y = kwargs.get("y")

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square instance """
        d = dict()
        for key, value in self.__dict__.items():
            split_string = list(key.split("_"))
            if split_string[-1] == "width" or split_string[-1] == "height":
                d["size"] = value
            else:
                d[split_string[-1]] = value
        return d
