#!/usr/bin/python3
def print_last_digit(number):
    last_num = int(str(number)[-1])
    print("{}".format(last_num), end="")
    return last_num
