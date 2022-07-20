#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        ex = Exception()
        if i > a:
            ex("Too far")
        else:
            result += (a * b) // i
            continue
        result = a + b
        break
    return result
