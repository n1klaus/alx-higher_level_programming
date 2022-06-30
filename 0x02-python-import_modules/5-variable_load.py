#!/usr/bin/python3
from variable_load_5 import a

"""Print variable from another module function
if inside the main module
"""

if __name__ == "__main__":
    print("{}".format(a))
else:
    print("{}".format(""), end="")