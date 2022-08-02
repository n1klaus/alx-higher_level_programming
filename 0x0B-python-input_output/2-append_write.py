#!/usr/bin/python3
""" Module to operate on a text file """


def append_write(filename="", text=""):
    """ Function to append a string at the end of a text file

    Args:
        filename (str): name of the file
        text (str): text to be written to file

    Returns:
        number of characters written to the file

    """
    num_char = 0
    if filename and text:
        with open(str(filename), mode="a", encoding="UTF-8") as o_file:
            num_char = o_file.write(str(text))
    return num_char
