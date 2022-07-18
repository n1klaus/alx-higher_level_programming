#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Function to raise a name exception with a message.

    Args:
        None

    Returns:
        Nothing
    """
    try:
        raise
    except Exception as e:
        print("{}".format(message))
