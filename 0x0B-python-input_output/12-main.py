#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    s = " "
    ss = "  "
    y = int(len(triangle) - 1)
    if y > 5:
        s = ss
    for row in triangle:
        # print("[{}]".format(",".join([str(x) for x in row])))
        for x in range(len(row)):
            if x == 0 and x == len(row) - 1:
                print("{0}{1}".format(s * y, row[x]), end="")
                y -= 1
            elif x == 0 and x != len(row) - 1:
                print("{0}{1}".format(s * y, row[x]), end=s)
                y -= 1
            elif x != 0 and x < len(row) - 1:
                print("{}".format(row[x]), end=s)
            else:
                print("{}".format(row[x]), end="")
        print()


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
