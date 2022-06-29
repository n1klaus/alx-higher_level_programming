#!/usr/bin/python3
import sys


def print_stderr(str):
    sys.stderr.write(f"{str}\n")
    exit(1)


print_stderr("and that piece of art is useful - Dora Korpar, 2015-10-19")
