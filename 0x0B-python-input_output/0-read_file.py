#!/usr/bin/python3
""" Module to operate on a text file """


def read_file(filename=""):
    """ Function to read a text file and print it to stdout

    Args:
        filename (str): name of the file

    """
    if filename:
        with open(str(filename), mode="r", encoding="utf-8") as o_file:
            print("{}".format(o_file.read()), end="")
        print("".format())
