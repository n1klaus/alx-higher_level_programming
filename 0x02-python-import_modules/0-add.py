#!/usr/bin/python3
from add_0 import add

"""Print addition function
if inside the main module
"""

a = 1
b = 2
c = add(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, c))
else:
    print("{}".format(""), end="")
