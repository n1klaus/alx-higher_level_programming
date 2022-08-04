#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function to convert a Roman numeral to an integer

    Args:
        roman_string (str): a string of roman characters

    Returns:
        int: integer value of roman string

    """
    val = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(roman_string) > 0 and isinstance(roman_string, str):
        for index in range(len(roman_string)):
            for k, v in romans.items():
                if roman_string[index] == k:
                    if index != len(roman_string) - 1:
                        if k == "C":
                            if roman_string[index + 1] == "M":
                                val += 900
                                index += 1
                                break
                            elif roman_string[index + 1] == "D":
                                val += 400
                                index += 1
                                break
                        elif k == "X":
                            if roman_string[index + 1] == "C":
                                val += 90
                                index += 1
                                break
                            elif roman_string[index + 1] == "L":
                                val += 40
                                index += 1
                                break
                        elif k == "I":
                            if roman_string[index + 1] == "X":
                                val += 9
                                index += 1
                                break
                            elif roman_string[index + 1] == "V":
                                val += 4
                                index += 1
                                break
                        val += v
                        break
                    else:
                        val += v
                        break
    return int(val)
