#!/usr/bin/Python3
def remove_char_at(str, n):
    for index in range(len(str)):
        if index == n:
            str = str.replace(str[index], "")
    return str
