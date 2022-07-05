#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My tuple adding function

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        tuple with results from addition
    """
    total_sum = 0, 0
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        total_sum = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    else:
        tuple_a += 0, 0
        tuple_b += 0, 0
        total_sum = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return total_sum
