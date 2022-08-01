#!/usr/bin/python3
""" Module to define list subclass """


class MyList(list):
    """ Subclass to list

    Args:
        list: a python list class

    """
    def __init__(self):
        """ Constructor to instantiate new class objects """
        super().__init__()

    def print_sorted(self):
        """ Function to print a list in a sorted manner """
        print("{}".format(sorted(self)))
