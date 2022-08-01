#!/usr/bin/python3
""" Module to define int subclass """


class MyInt(int):
    """ Subclass to int

    Attributes:
        __value (int): an integer number

    """
    def __init__(self, value):
        """ Constructor to instantiate new class objects

        Args:
            value (int): an integer number

        """
        super().__init__()
        self.__value = value

    def __eq__(self, other):
        """ Method to define inverted equal operator """
        if self.__value == other:
            return False
        return True

    def __ne__(self, other):
        """ Method to define inverted not equal operator """
        if self.__value != other:
            return False
        return True
