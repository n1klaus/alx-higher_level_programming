#!/usr/bin/python3
""" Module to define a matrix multiplying function """


def matrix_mul(m_a, m_b):
    """Function to multiply two matrix

    Args:
        m_a (:obj:list of lists of 'int' or 'float):
        a 2 dimensional list of lists
        m_b (:obj:list of lists of 'int' or 'float):
        a 2 dimensional list of lists

    Returns:
        new matrix with the new results

    """
    isCalculated = False
    product = 0
    inner_product = []
    result = []

    if isinstance(m_a, (list)):
        if isinstance(m_b, (list)):
            if isinstance(m_a[0], (list)):
                if isinstance(m_b[0], (list)):
                    if m_a or m_a[0]:
                        if m_b or m_b[0]:
                            for row in range(len(m_a)):
                                if row < (len(m_a[row]) - 1) and\
                                        len(m_a[row]) != len(m_a[row + 1]):
                                    raise TypeError('''each row of m_a must be\
                                    of the same size''')
                                for column in range(len(m_a[row])):
                                    isCalculated = False
                                    if not isinstance(column, (int, float)):
                                        raise TypeError("m_a should contain\
                                        only integers or floats")
                                    for r in range(len(m_b)):
                                        if r < (len(m_b[r]) - 1) and\
                                                len(m_b[r]) != len(m_b[r + 1]):
                                            raise TypeError('''each row of m_b\
                                            must be of the same size''')
                                        for c in range(len(m_b[r])):
                                            if not isinstance(c, (int, float)):
                                                raise TypeError('''m_b should\
                                                    contain only integers or\
                                                    floats''')
                                            if c == row and r == column:
                                                product += (column * c)
                                                isCalculated = True
                                                break
                                        if (isCalculated):
                                            inner_product.append(product)
                                            break
                            result.append(inner_product)
                        else:
                            raise ValueError("m_b can't be empty")
                    else:
                        raise ValueError("m_a can't be empty")
                else:
                    raise TypeError("m_b must be a list of lists")
            else:
                raise TypeError("m_a must be a list of lists")
        else:
            raise TypeError("m_b must be a list".format())
    else:
        raise TypeError("m_a must be a list".format())
    return result


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/100-matrix_mul.txt')
