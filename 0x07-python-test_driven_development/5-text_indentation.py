#!/usr/bin/python3
""" Module to define an text indentation function """


def text_indentation(text):
    """Function to print adds new lines after text with
    characters '.' '?' ':'

    Args:
        text ('str'): a string of characters

    """
    new_str = ""
    if isinstance(text, str):
        for char in range(len(text)):
            if text[char] in '.?:':
                new_str += text[char] + '\n\n'
                if text[char+1].isspace():
                    new_str += ''
            else:
                if text[char].isspace():
                    new_str += ''
                else:
                    new_str += text[char]
        print("{}".format(new_str), end="")
    else:
        raise TypeError("text must be a string")


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
