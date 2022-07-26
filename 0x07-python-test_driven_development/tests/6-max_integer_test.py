#!/usr/bin/python3
""" Module to define a unittest testcase """


import unittest
class TestMaxInteger(unittest.TestCase):
    """Class definition for testcase on def max_integer(list=[])

    """
    def test_isList(self):
        list1 = []
        self.assertEqual(isinstance(list1, list), True)

    def test_listIsEmpty(self):
        list = []
        self.assertEqual(len(list), 0)

    def test_isIntegerList(self):
        list = [1, 2, 3]
        for i in list:
            self.assertEqual(isinstance(i, int), True)

    def test_isEqual(self):
        list = [1, 1]
        for i in range(len(list)):
            if i < len(list) - 1 and list[i] == list[i + 1]:
                self.assertEqual(self, True)

    def test_isLarger(self):
        list = [3, 2, 1]
        for i in range(len(list)):
            if i < len(list) - 1 and list[i] > list[i + 1]:
                self.assertEqual(self, True)

if __name__ == '__main__':
    unittest.main()
