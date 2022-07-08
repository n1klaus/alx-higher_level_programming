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
        for char in range(len(roman_string)):
            for r in list(romans.items()):
                if roman_string[char] is r[0]:
                    if roman_string[char] == "I" and \
                            char < len(roman_string) - 1:
                        if roman_string[char + 1] == "V":
                            val += 4
                            return int(val)
                        elif roman_string[char + 1] == "X":
                            val += 9
                            return int(val)
                    val += r[1]
    return int(val)
