#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My tuple adding function

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        tuple with results from addition
    """
    if len(tuple_a) >= 2 and len(tuple_a) >= 2:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_a[1] + tuple_b[1]
    elif not tuple_a[0] or not tuple_b[0]:
        sum1 = tuple_a[0] + 0 if not tuple_a[0] else tuple_b[0] + 0
    elif not tuple_a[1] or not tuple_b[1]:
        sum2 = tuple_a[1] + 0 if not tuple_a[1] else tuple_b[1] + 0
    return sum1, sum2
