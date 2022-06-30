#!/usr/bin/python3
from email.policy import default
from sys import argv
from calculator_1 import add, sub, mul, div


def my_calculator(argv):
    """My calculator function

    Args:
        argv: list of command line arguments

    Returns:
        The exit status
    """

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    match operator:
        case "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /"
                  .format(""))
            exit(1)
    exit(0)


if __name__ == "__main__":
    my_calculator(argv)
else:
    print("{}".format(""), end="")
