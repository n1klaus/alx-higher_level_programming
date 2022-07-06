#!/usr/bin/python3
def best_score(a_dictionary):
    """Function to return a key with the biggest integer value.

    Args:
        a_dictionary: a dictionary of key and value pairs

    Returns:
        key with highest score or
        None if no score is found
    """
    if a_dictionary:
        vals = sorted(list(a_dictionary.values()))
        items = list(a_dictionary.items())
        for tup in items:
            if tup[1] is vals[-1]:
                return tup[0]
    else:
        return None
