#!/usr/bin/python3
from sys import argv


def add_argv():
    """Print result of addedd list of arguments function
    """

    if __name__ == "__main__":
        total = 0
        if len(argv) == 1:
            print("{}".format(total))
        else:
            i = 1
            for count in range(len(argv) - 1):
                total += int(argv[i])
                i += 1
            print("{}".format(total))
    else:
        print("{}".format(""), end="")


add_argv()
