#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function to divide element by element from 2 lists.

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of the new list

    Returns:
        new list of length list_length with the values from the division
    """
    new_list = []
    try:
        for i in range(len(my_list_1)):
            if isinstance(my_list_1[i], int) and\
                    isinstance(my_list_2[i], int):
                new_list.append(my_list_1[i] / my_list_2[i])
    except ZeroDivisionError:
        new_list.append(0)
        print("division by 0".format())
    except TypeError:
        new_list.append(0)
        print("wrong type".format())
    except IndexError:
        new_list.append(0)
        print("out of range".format())
    except Exception as e:
        raise
    finally:
        return new_list
