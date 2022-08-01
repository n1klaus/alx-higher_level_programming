#!/usr/bin/python3
""" Module to define Geometry class """


class BaseGeometry:
    """ Class definition for geometry calculations """

    def __init__(self):
        """ Empty constructor for initializing class instances """
        pass

    def area(self):
        """ Raise an Exception with the defined custom message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method to validate the value provided

        Args:
            name (str): string of characters
            value: integer number

        """
        if value.__class__ is int:
            if value > 0:
                pass
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
