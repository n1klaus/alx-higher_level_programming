#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Function to replaces all occurrences of an element by another in
    a new list

    Args:
        my_list: list of elements
        search: element to search
        replace: element to replace with

    Returns:
        new list with the replaced values
    """
    new_list = my_list.copy()
    for elem in new_list:
        if elem is search:
            for pos in range(new_list.count(search)):
                i = new_list.index(search, pos)
                new_list[i] = replace
    return new_list
