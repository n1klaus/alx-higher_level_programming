#!/usr/bin/python3
def print_reverse_alpha():
    str = ""
    for c in range(122, 96, -1):
        if c % 2 != 0:
            str += chr(c - 32)
        else:
            str += chr(c)
    print("{}".format(str), end="")


print_reverse_alpha()
