#!/usr/bin/python3
def multiple_returns(sentence):
    """My tuple length and first character printing function

    Args:
        sentence: character string

    Returns:
        length of tuple and the first character
    """
    for first_word in sentence.split():
        first_char = first_word[0]
    length = len(sentence)
    return length, first_char
