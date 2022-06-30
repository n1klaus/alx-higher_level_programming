#!/usr/bin/python3
from sys import argv


def print_argv():
    """Print list of arguments function
    """

    if __name__ == "__main__":
        i = 1
        if len(argv) == 1:
            print("{} arguments.".format(len(argv) - 1))
        elif len(argv) == 2:
            print("{} argument:".format(len(argv) - 1))
            print("{}: {}".format(i, argv[i]))
        else:
            print("{} arguments:".format(len(argv) - 1))
            for count in range(len(argv) - 1):
                print("{}: {}".format(i, argv[i]))
                i += 1
    else:
        print("{}".format(""), end="")


print_argv()
