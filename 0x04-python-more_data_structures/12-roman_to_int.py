#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function to convert a Roman numeral to an integer

    Args:
	    roman_string: a string of roman characters

    Returns:
        integer value of roman string
    """
    val = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if type(roman_string) is str and roman_string is not None:
        for r in list(romans.items()):
            for char in roman_string:
                if r[0] is char:
                    val += r[1]
    return val


