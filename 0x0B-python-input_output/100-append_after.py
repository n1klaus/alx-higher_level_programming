#!/usr/bin/python3
""" Module to define text file insertion """


def append_after(filename="", search_string="", new_string=""):
    """ Insert text after each line containing a given string in a file

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.

    """
    text = ""
    try:
        with open(filename, mode="r", encoding="UTF-8") as r_file:
            for line in r_file:
                text += line
                if search_string in line:
                    text += new_string
        with open(filename, mode="w", encoding="UTF-8") as w_file:
            w_file.write(text)
    except Exception as e:
        raise
