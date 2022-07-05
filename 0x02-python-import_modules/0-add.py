#!/usr/bin/python3
from add_0 import add

"""Print addition function
if inside the main module
"""

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
else:
    print("{}".format(""), end="")
