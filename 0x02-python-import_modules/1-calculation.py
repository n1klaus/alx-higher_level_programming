#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

"""Print results from calculator function
if inside the main module
"""

a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
else:
    print("{}".format(""), end="")