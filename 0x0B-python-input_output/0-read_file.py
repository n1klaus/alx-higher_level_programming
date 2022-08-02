#!/usr/bin/python3
""" Module to operate on a text file """


def read_file(filename=""):
    """ Function to read a text file and print it to stdout

    Args:
        filename: name of the file

    """
    if filename:
        with open(filename, mode='r', encoding='UTF-8') as o_file:
            for line in o_file:
                print("{}".format(line), end="")
            print("".format())
