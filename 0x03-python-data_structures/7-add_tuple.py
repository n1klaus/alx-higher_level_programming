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
        for num1, num2 in tuple_a:
            for int1, int2 in tuple_b:
                sum1 = num1 + int1
                sum2 = num2 + int2
    elif len(tuple_a) < 2 or len(tuple_b) < 2:
        sum1 = tuple_a[0] + 0 if tuple_a else tuple_b[0] + 0
    else:
        sum2 = tuple_a[1] + 0 if tuple_a else tuple_b[1] + 0
    return sum1, sum2
