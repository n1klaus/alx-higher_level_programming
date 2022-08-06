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
