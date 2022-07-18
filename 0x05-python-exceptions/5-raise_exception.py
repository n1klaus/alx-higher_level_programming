#!/usr/bin/python3
def raise_exception():
    """Function to raise a type exception.

    Args:
        None

    Returns:
        Nothing
    """
    try:
        raise TypeError
    except Exception as e:
        raise
