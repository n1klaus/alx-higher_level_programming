#!/usr/bin/python3
""" Module to find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds the peak in list of unsorted integers """
    list_of_integers.sort()
    if not list_of_integers:
        return None
    else:
        return list_of_integers[-1]
