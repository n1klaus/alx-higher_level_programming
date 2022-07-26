#!/usr/bin/python3
""" Module to define a name printing function """


def say_my_name(first_name, last_name=""):
    """Function to print the first name and last name as provided

    Args:
        first_name ('str'): a string representing the first name
        last_name ('str', optional): a string representing the last name

    """
    if isinstance(first_name, (str)) and len(first_name) != 0 \
            and first_name.isalnum():
        if isinstance(last_name, (str)):
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
