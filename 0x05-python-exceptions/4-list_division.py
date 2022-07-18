#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function to divides element by element 2 lists.

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of the new list

    Returns:
        new list of length list_length with values of the division
    """
    new_list = []
    try:
        for i in range(max(list_length, len(my_list_1), len(my_list_2))):
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
