#!/usr/bin/python3
""" Module to operate on a text file """


def write_file(filename="", text=""):
    """ Function to write a string to a text file

    Args:
        filename (str): name of the file
        text (str): text to be written to file

    Returns:
        number of characters written to the file

    """
    num_char = 0
    if filename and text:
        with open(str(filename), mode="w", encoding="UTF-8") as o_file:
            num_char = o_file.write(text)
    return num_char
