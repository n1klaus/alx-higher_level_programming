#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My tuple adding function

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        tuple with results from addition
    """
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_a[1] + tuple_b[1]
    else:
        if len(tuple_a) == 1:
            sum1 = tuple_a[0] + tuple_b[0]
            sum2 = tuple_b[1] + 0
        elif len(tuple_b) == 1:
            sum1 = tuple_a[0] + tuple_b[0]
            sum2 = tuple_a[1] + 0
        elif len(tuple_a) == 0:
            sum1 = tuple_b[0] + 0
            sum2 = tuple_b[1] + 0
        elif len(tuple_b) == 0:
            sum1 = tuple_a[0] + 0
            sum2 = tuple_a[1] + 0
    return sum1, sum2
