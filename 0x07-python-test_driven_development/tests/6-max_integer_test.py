#!/usr/bin/python3
""" Module to define a unittest testcase """


import unittest


class TestMaxInteger(unittest.TestCase):
    """Class definition for testcase on 'max_integer(list=[])'

    """
    def test_isList(self):
        list1 = []
        self.assertIsInstance(list1, list)

    def test_listIsEmpty(self):
        list = []
        self.assertTrue(len(list) == 0)

    def test_listIsNotEmpty(self):
        list = [1]
        self.assertTrue(len(list) > 0)

    def test_isIntegerList(self):
        list = [1, 2, 3]
        for i in list:
            self.assertIsInstance(i, int)

    def test_ItemisEqual(self):
        list = [1, 1]
        for index in range(len(list)):
            if index < len(list) - 1 and list[index] == list[index + 1]:
                self.assertEqual(list[index], list[index + 1])

    def test_ItemisLarger(self):
        list = [3, 2, 1]
        for index in range(len(list)):
            if index < len(list) - 1 and list[index] > list[index + 1]:
                self.assertGreater(list[index], list[index + 1])

    def test_ItemisSmaller(self):
        list = [1, 2, 3]
        for index in range(len(list)):
            if index < len(list) - 1 and list[index] < list[index + 1]:
                self.assertLess(list[index], list[index + 1])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMaxInteger('6-max_integer'))
    return suite


if __name__ == '__main__':
    runner = unittest.TestRunner()
    runner.run(suite())
