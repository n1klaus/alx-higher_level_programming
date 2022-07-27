#!/usr/bin/python3
""" Module to define a locked class """


class LockedClass:
    """ Allows only use of the first_name instance attribute while any other
    creation or change of attributes is locked"""

    __slots__ = "first_name"
