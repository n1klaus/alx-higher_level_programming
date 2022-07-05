#!/usr/bin/python3
from add_0 import add

"""Print addition function
if inside the main module
"""

a = 1
b = 2
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
else:
    print("{}".format(""), end="")
