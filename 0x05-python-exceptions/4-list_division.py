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
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0".format())
        except TypeError:
            result = 0
            print("wrong type".format())
        except IndexError:
            result = 0
            print("out of range".format())
        except Exception as e:
            raise
        finally:
            new_list.append(result)
    return new_list
