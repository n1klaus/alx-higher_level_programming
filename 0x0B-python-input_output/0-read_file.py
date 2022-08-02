#!/usr/bin/python3
""" Module to oprate on a text file """


def read_file(filename=""):
    """ Function to read a text file and print it to stdout

    Args:
        filename: name of the file

    """
    with open(filename, mode='r', encoding='UTF-8') as o_file:
        print(o_file.read())
