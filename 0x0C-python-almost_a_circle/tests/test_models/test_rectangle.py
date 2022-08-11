#!/usr/bin/python3
""" Defines unittests for rectangle.py """
import unittest
import json
import os
from models.rectangle import Rectangle


class TestRectangle__init__(unittest.TestCase):
    """ Unittests for testing the constructor of the Rectangle class
        public method '__init__(self, width, height, x=0, y=0, id=None)'

        Note:
            Only 2 positional arguments are required, other 3 are optional

    """

    def test_ID_automatic_assignment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertGreater(r2.id, r1.id)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None, None)

    def test_list(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], [1, 2, 3])

    def test_bool_true(self):
        r1 = Rectangle(True, True)
        self.assertIsInstance(r1, Rectangle)

    def test_bool_false(self):
        with self.assertRaises(ValueError):
            Rectangle(False, False)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_positive_number(self):
        r1 = Rectangle(4, 4)
        self.assertIsInstance(r1, Rectangle)

    def test_negative_number_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_number_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_negative_number_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_number_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_negative_number_id(self):
        with self.assertRaises(AssertionError):
            Rectangle(1, 2, 3, 4, -5)

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(4.99999, 4.99999)

    def test_str_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_str_id(self):
        with self.assertRaises(AssertionError):
            Rectangle(1, 2, 3, 4, "5")

    def test_complex(self):
        with self.assertRaises(TypeError):
            Rectangle(complex(5), complex(5))

    def test_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(("4", 4), ("4", 4))

    def test_dict(self):
        with self.assertRaises(TypeError):
            Rectangle({"id": 4}, {"id": 4})

    def test_set(self):
        with self.assertRaises(TypeError):
            Rectangle({12, 24, 36}, {12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(TypeError):
            Rectangle(frozenset({12, 24, 36}), frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(TypeError):
            Rectangle(range(5), range(10))

    def test_bytes(self):
        with self.assertRaises(TypeError):
            Rectangle(b'AtoZ', b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(TypeError):
            Rectangle(bytearray(b'AtoZ'), bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(TypeError):
            Rectangle(memoryview(b'AtoZ'), memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('Inf'), float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-Inf'), float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(TypeError):
            Rectangle(float('NaN'), float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        self.assertIsInstance(r1, Rectangle)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r1, Rectangle)

    def test_five_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1, Rectangle)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)


class TestRectangle_width_setter(unittest.TestCase):
    """ Unittests for testing 'width(self, value)'
        public setter method of the Rectangle class

    """

    def test_no_value_assignment(self):
        r1 = Rectangle(8, 4)
        r1.width
        self.assertIsInstance(r1.width, int)
        self.assertEqual(r1.width, 8)

    def test_more_value_assignment(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = 1, 2, 3

    def test_None(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = None

    def test_list(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = [1, 2, 3]

    def test_bool_true(self):
        r1 = Rectangle(8, 4)
        r1.width = True
        self.assertIsInstance(r1.width, int)
        self.assertTrue(r1.width)

    def test_bool_false(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(ValueError):
            r1.width = False

    def test_positive_number(self):
        r1 = Rectangle(8, 4)
        r1.width = 4
        self.assertIsInstance(r1.width, int)
        self.assertEqual(r1.width, 4)

    def test_negative_number(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(ValueError):
            r1.width = -4

    def test_float(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = 4.99999

    def test_complex(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = complex(5)

    def test_str(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = "4"

    def test_tuple(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = (4, 4)

    def test_dict(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = {"id": 4}

    def test_set(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = {12, 24, 36}

    def test_frozenset(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = frozenset({12, 24, 36})

    def test_range(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = range(10)

    def test_bytes(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = b'AtoZ'

    def test_bytearray(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = bytearray(b'AtoZ')

    def test_memoryview(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = memoryview(b'AtoZ')

    def test_Inf(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = float('Inf')

    def test_negative_Inf(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = float('-Inf')

    def test_NaN(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.width = float('NaN')


class TestRectangle_height_setter(unittest.TestCase):
    """ Unittests for testing 'height(self, value)'
        public setter method of Rectangle class

    """

    def test_no_value_assignment(self):
        r1 = Rectangle(8, 4)
        r1.height
        self.assertIsInstance(r1.height, int)
        self.assertEqual(r1.height, 4)

    def test_more_value_assignment(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = 1, 2, 3

    def test_None(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = None

    def test_list(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = [1, 2, 3]

    def test_bool_true(self):
        r1 = Rectangle(8, 4)
        r1.height = True
        self.assertIsInstance(r1.height, int)
        self.assertTrue(r1.height)

    def test_bool_false(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(ValueError):
            r1.height = False

    def test_positive_number(self):
        r1 = Rectangle(8, 4)
        r1.height = 4
        self.assertIsInstance(r1.height, int)
        self.assertEqual(r1.height, 4)

    def test_negative_number(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(ValueError):
            r1.height = -4

    def test_float(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = 4.99999

    def test_complex(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = complex(5)

    def test_str(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = "4"

    def test_tuple(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = (4, 4)

    def test_dict(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = {"id": 4}

    def test_set(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = {12, 24, 36}

    def test_frozenset(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = frozenset({12, 24, 36})

    def test_range(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = range(10)

    def test_bytes(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = b'AtoZ'

    def test_bytearray(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = bytearray(b'AtoZ')

    def test_memoryview(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = memoryview(b'AtoZ')

    def test_Inf(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = float('Inf')

    def test_negative_Inf(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = float('-Inf')

    def test_NaN(self):
        r1 = Rectangle(8, 4)
        with self.assertRaises(TypeError):
            r1.height = float('NaN')


class TestRectangle_x_setter(unittest.TestCase):
    """ Unittests for testing 'x(self, value)'
        public setter method of Rectangle class

    """

    def test_no_value_assignment(self):
        r1 = Rectangle(8, 4, 1)
        r1.x
        self.assertIsInstance(r1.x, int)
        self.assertEqual(r1.x, 1)

    def test_more_value_assignment(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = 1, 2, 3

    def test_None(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = None

    def test_list(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = [1, 2, 3]

    def test_bool_true(self):
        r1 = Rectangle(8, 4, 1)
        r1.x = True
        self.assertIsInstance(r1.x, int)
        self.assertTrue(r1.x)

    def test_bool_false(self):
        r1 = Rectangle(8, 4, 1)
        r1.x = False
        self.assertIsInstance(r1.x, int)
        self.assertFalse(r1.x)

    def test_positive_number(self):
        r1 = Rectangle(8, 4, 1)
        r1.x = 4
        self.assertIsInstance(r1.x, int)
        self.assertEqual(r1.x, 4)

    def test_negative_number(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(ValueError):
            r1.x = -4

    def test_float(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = 4.99999

    def test_complex(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = complex(5)

    def test_str(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = "4"

    def test_tuple(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = (4, 4)

    def test_dict(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = {"id": 4}

    def test_set(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = {12, 24, 36}

    def test_frozenset(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = frozenset({12, 24, 36})

    def test_range(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = range(10)

    def test_bytes(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = b'AtoZ'

    def test_bytearray(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = bytearray(b'AtoZ')

    def test_memoryview(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = memoryview(b'AtoZ')

    def test_Inf(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = float('Inf')

    def test_negative_Inf(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = float('-Inf')

    def test_NaN(self):
        r1 = Rectangle(8, 4, 1)
        with self.assertRaises(TypeError):
            r1.x = float('NaN')


class TestRectangle_y_setter(unittest.TestCase):
    """ Unittests for testing 'y(self, value)'
        public setter method of Rectangle class

    """

    def test_no_value_assignment(self):
        r1 = Rectangle(8, 4, 1, 3)
        r1.y
        self.assertIsInstance(r1.y, int)
        self.assertEqual(r1.y, 3)

    def test_more_value_assignment(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = 1, 2, 3

    def test_None(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = None

    def test_list(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = [1, 2, 3]

    def test_bool_true(self):
        r1 = Rectangle(8, 4, 1, 3)
        r1.y = True
        self.assertIsInstance(r1.y, int)
        self.assertTrue(r1.y)

    def test_bool_false(self):
        r1 = Rectangle(8, 4, 1, 3)
        r1.y = False
        self.assertIsInstance(r1.y, int)
        self.assertFalse(r1.y)

    def test_positive_number(self):
        r1 = Rectangle(8, 4, 1, 3)
        r1.y = 4
        self.assertIsInstance(r1.y, int)
        self.assertEqual(r1.y, 4)

    def test_negative_number(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(ValueError):
            r1.y = -4

    def test_float(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = 4.99999

    def test_complex(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = complex(5)

    def test_str(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = "4"

    def test_tuple(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = (4, 4)

    def test_dict(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = {"id": 4}

    def test_set(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = {12, 24, 36}

    def test_frozenset(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = frozenset({12, 24, 36})

    def test_range(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = range(10)

    def test_bytes(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = b'AtoZ'

    def test_bytearray(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = bytearray(b'AtoZ')

    def test_memoryview(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = memoryview(b'AtoZ')

    def test_Inf(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = float('Inf')

    def test_negative_Inf(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = float('-Inf')

    def test_NaN(self):
        r1 = Rectangle(8, 4, 1, 3)
        with self.assertRaises(TypeError):
            r1.y = float('NaN')


class TestRectangle_area(unittest.TestCase):
    """ Unittests for testing 'area(self)'
        public method of Rectangle class

    """

    def test_output_type(self):
        a = Rectangle(8, 4, 1, 3).area()
        self.assertIsInstance(a, int)

    def test_no_args(self):
        a = Rectangle(8, 4, 1, 3).area()
        self.assertEqual(a, 32)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).area(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).area(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).area(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).area(False)


class TestRectangle_display(unittest.TestCase):
    """ Unittests for testing 'display(self)'
        public method of Rectangle class

    """

    def test_output_type(self):
        d = Rectangle(8, 4, 1, 3).display()
        self.assertIsNone(d)

    def test_no_x(self):
        d = Rectangle(8, 4, x=2).display()
        self.assertIsNone(d)

    def test_no_y(self):
        d = Rectangle(8, 4, y=4).display()
        self.assertIsNone(d)

    def test_no_x_and_no_y(self):
        d = Rectangle(8, 4).display()
        self.assertIsNone(d)

    def test_no_args(self):
        d = Rectangle(8, 4).display()
        self.assertIsNone(d)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).display(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).display(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).display(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3).display(False)


class TestRectangle__str__(unittest.TestCase):
    """ Unittests for testing '__str__(self)'
        public method of Rectangle class

    """

    def test_output_type(self):
        s = Rectangle(8, 4, 1, 3, 55).__str__()
        self.assertIsNotNone(s)
        self.assertIsInstance(s, str)

    def test_no_args(self):
        s = Rectangle(8, 4, 1, 3, 55).__str__()
        self.assertEqual(s, "[Rectangle] (55) 1/3 - 8/4")

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).__str__(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).__str__(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).__str__(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).__str__(False)


class TestRectangle_update(unittest.TestCase):
    """ Unittests for testing 'update(self, *args, **kwargs)'
        public method of Rectangle class

    """

    def test_output_type(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = [1, 2, 3, 4, 5]
        ar = r1.update(*args)
        self.assertIsNone(ar)

    def test_None(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = None
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_list(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = [1, 2, 3, 4, 5]
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_bool_true(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = True
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_bool_false(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = False
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_insert_number_id(self):
        r1 = Rectangle(8, 4, 1, 3, 55).update(89)
        self.assertEqual(r1.__str__(), 'None')

    def test_insert_number_width(self):
        r1 = Rectangle(8, 4, 1, 3, 55).update(89, 1)
        self.assertEqual(r1.__str__(), 'None')

    def test_insert_number_height(self):
        r1 = Rectangle(8, 4, 1, 3, 55).update(89, 1, 2)
        self.assertEqual(r1.__str__(), 'None')

    def test_insert_number_x(self):
        r1 = Rectangle(8, 4, 1, 3, 55).update(89, 1, 2, 3)
        self.assertEqual(r1.__str__(), 'None')

    def test_insert_number_y(self):
        r1 = Rectangle(8, 4, 1, 3, 55).update(89, 1, 2, 3, 4)
        self.assertEqual(r1.__str__(), 'None')

    def test_positive_number(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = 4
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_negative_number(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = -4
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_float(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = 4.99999
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_complex(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = complex(5)
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_str(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = "4"
        with self.assertRaises(AssertionError):
            r1.update(*args)

    def test_tuple(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = (1, 2, 3, 4, 5)
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_dict_id(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update(**{"id": 1})
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/3 - 8/4')

    def test_dict_width(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update(**{"id": 1, "width": 2})
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/3 - 2/4')

    def test_dict_height(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update(**{"id": 1, "width": 2, "height": 3})
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/3 - 2/3')

    def test_dict_x(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update(**{"id": 1, "width": 2, "height": 3, "x": 4})
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/3 - 2/3')

    def test_dict_y(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update(**{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_set(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = {1, 2, 3, 4, 5}
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_frozenset(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = frozenset({1, 2, 3, 4, 5})
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_range(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = range(5)
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (0) 3/4 - 1/2')

    def test_bytes(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = b'AtoZ'
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (65) 90/3 - 116/111')

    def test_bytearray(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = bytearray(b'AtoZ')
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (65) 90/3 - 116/111')

    def test_memoryview(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = memoryview(b'AtoZ')
        r1.update(*args)
        self.assertEqual(r1.__str__(), '[Rectangle] (65) 90/3 - 116/111')

    def test_Inf(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = float('Inf')
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_negative_Inf(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = float('-Inf')
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_NaN(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        args = float('NaN')
        with self.assertRaises(TypeError):
            r1.update(*args)

    def test_no_args(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        r1.update()
        self.assertEqual(r1.__str__(), '[Rectangle] (55) 1/3 - 8/4')


class TestRectangle_to_dictionary(unittest.TestCase):
    """ Unittests for testing 'to_dictionary(self)'
        public method of Rectangle class

    """

    def test_output_type(self):
        d = Rectangle(8, 4, 1, 3, 55).to_dictionary()
        self.assertIsInstance(d, dict)

    def test_no_args(self):
        d = Rectangle(8, 4, 1, 3, 55).to_dictionary()
        self.assertIsNotNone(d)
        self.assertDictEqual(d,
                             {
                                'id': 55,
                                'width': 8,
                                'height': 4,
                                'x': 1,
                                'y': 3
                             })

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).to_dictionary(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).to_dictionary(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).to_dictionary(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 4, 1, 3, 55).to_dictionary(False)


class TestRectangle_to_json_string(unittest.TestCase):
    """ Unittests for testing 'to_json_string(list_dictionaries)'
        static method of the Rectangle class

    """

    def test_empty_list(self):
        self.assertEqual("[]", Rectangle.to_json_string([]))

    def test__None(self):
        self.assertEqual("[]", Rectangle.to_json_string(None))

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(True)

    def test_bool_false(self):
        self.assertEqual("[]", Rectangle.to_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Rectangle.to_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle.to_json_string([], [])


class TestRectangle_save_to_file(unittest.TestCase):
    """ Unittests for testing 'save_to_file(cls, list_objs)'
        class method for Rectangle class

    """

    @classmethod
    def tearDown(self):
        """ Delete created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_create_new_file(self):
        r1 = Rectangle(12, 20, 1, 1, 19)
        Rectangle.save_to_file([r1])
        stream = str()
        with open("Rectangle.json", "r") as f:
            stream += f.read()
        res = json.loads(stream)
        self.assertEqual(res[0].get('id'), 19)
        self.assertEqual(res[0].get('_Rectangle__width'), 12)
        self.assertEqual(res[0].get('_Rectangle__height'), 20)
        self.assertEqual(res[0].get('_Rectangle__x'), 1)
        self.assertEqual(res[0].get('_Rectangle__y'), 1)

    def test_overwrite_file(self):
        r1 = Rectangle(24, 30, 2, 3, 11)
        r2 = Rectangle(36, 40, 5, 6, 8)
        Rectangle.save_to_file([r1])
        stream1 = str()
        with open("Rectangle.json", "r") as f1:
            stream1 += f1.read()
        res = json.loads(stream1)
        self.assertEqual(res[0].get('id'), 11)
        self.assertEqual(res[0].get('_Rectangle__width'), 24)
        self.assertEqual(res[0].get('_Rectangle__height'), 30)
        self.assertEqual(res[0].get('_Rectangle__x'), 2)
        self.assertEqual(res[0].get('_Rectangle__y'), 3)
        Rectangle.save_to_file([r2])
        stream2 = str()
        with open("Rectangle.json", "r") as f2:
            stream2 += f2.read()
        res = json.loads(stream2)
        self.assertEqual(res[0].get('id'), 8)
        self.assertEqual(res[0].get('_Rectangle__width'), 36)
        self.assertEqual(res[0].get('_Rectangle__height'), 40)
        self.assertEqual(res[0].get('_Rectangle__x'), 5)
        self.assertEqual(res[0].get('_Rectangle__y'), 6)

    def test_None(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(None)

    def test_empty_list(self):
        Rectangle.save_to_file([])
        stream = str()
        with open("Rectangle.json", "r") as f:
            stream += f.read()
        self.assertEqual("[]", stream)

    def test_list_rectangle(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        stream = str()
        with open("Rectangle.json", "r") as f:
            stream += f.read()
        self.assertEqual(len(str(Rectangle(1, 2).__dict__)) + 2, len(stream))

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(True)

    def test_bool_false(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(False)

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([1], [12])


class TestRectangle_from_json_string(unittest.TestCase):
    """ Unittests for testing 'from_json_string(json_string)'
        static method of Rectangle class

    """

    def test_output_type(self):
        list_output = Rectangle.from_json_string('[{"id": 4}]')
        self.assertIsInstance(list_output, list)

    def test_None(self):
        self.assertEqual([], Rectangle.from_json_string(None))

    def test_empty_list(self):
        self.assertEqual([], Rectangle.from_json_string("[]"))

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(True)

    def test_bool_false(self):
        self.assertEqual([], Rectangle.from_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(-4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string("4")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Rectangle.from_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Rectangle.from_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string([], 4)


class TestRectangle_create(unittest.TestCase):
    """ Unittests for testing 'create(cls, **dictionary)'
        class method of Rectangle class

    """

    def test_None(self):
        kwargs = None
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_empty_dictionary(self):
        kwargs = {}
        r1 = Rectangle(1, 2)
        r2 = r1.create(**kwargs)
        self.assertIsInstance(r2, Rectangle)

    def test_dict_id(self):
        kwargs = {'id': 89}
        r1 = Rectangle(1, 2)
        r2 = r1.create(**kwargs)
        self.assertEqual(r2.__dict__.get('id'), kwargs.get('id'))

    def test_dict_width(self):
        r1 = Rectangle(1, 2)
        kwargs = {'id': 89, 'width': 1}
        r2 = r1.create(**kwargs)
        self.assertEqual(r2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(r2.__dict__.get('_Rectangle__width'),
                         kwargs.get('width'))

    def test_dict_height(self):
        r1 = Rectangle(1, 2)
        kwargs = {'id': 89, 'width': 1, 'height': 2}
        r2 = r1.create(**kwargs)
        self.assertEqual(r2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(r2.__dict__.get('_Rectangle__width'),
                         kwargs.get('width'))
        self.assertEqual(r2.__dict__.get('_Rectangle__height'),
                         kwargs.get('height'))

    def test_dict_x(self):
        r1 = Rectangle(1, 2)
        kwargs = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r2 = r1.create(**kwargs)
        self.assertEqual(r2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(r2.__dict__.get('_Rectangle__width'),
                         kwargs.get('width'))
        self.assertEqual(r2.__dict__.get('_Rectangle__height'),
                         kwargs.get('height'))
        self.assertEqual(r2.__dict__.get('_Rectangle__x'), kwargs.get('x'))

    def test_dict_y(self):
        r1 = Rectangle(1, 2)
        kwargs = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r2 = r1.create(**kwargs)
        self.assertEqual(r2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(r2.__dict__.get('_Rectangle__width'),
                         kwargs.get('width'))
        self.assertEqual(r2.__dict__.get('_Rectangle__height'),
                         kwargs.get('height'))
        self.assertEqual(r2.__dict__.get('_Rectangle__x'), kwargs.get('x'))
        self.assertEqual(r2.__dict__.get('_Rectangle__y'), kwargs.get('y'))

    def test_bool_true(self):
        r1 = Rectangle(1, 2)
        kwargs = True
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_bool_false(self):
        r1 = Rectangle(1, 2)
        kwargs = False
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_positive_number(self):
        r1 = Rectangle(1, 2)
        kwargs = 4
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_negative_number(self):
        r1 = Rectangle(1, 2)
        kwargs = -4
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_float(self):
        r1 = Rectangle(1, 2)
        kwargs = 4.99999
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_complex(self):
        r1 = Rectangle(1, 2)
        kwargs = complex(5)
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_str(self):
        r1 = Rectangle(1, 2)
        kwargs = "4"
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_tuple(self):
        r1 = Rectangle(1, 2)
        kwargs = ("4", 4)
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_set(self):
        r1 = Rectangle(1, 2)
        kwargs = {12, 24, 36}
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_frozenset(self):
        r1 = Rectangle(1, 2)
        kwargs = frozenset({12, 24, 36})
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_range(self):
        r1 = Rectangle(1, 2)
        kwargs = range(5)
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_bytes(self):
        r1 = Rectangle(1, 2)
        kwargs = b'AtoZ'
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_bytearray(self):
        r1 = Rectangle(1, 2)
        kwargs = bytearray(b'AtoZ')
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_memoryview(self):
        r1 = Rectangle(1, 2)
        kwargs = memoryview(b'AtoZ')
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_Inf(self):
        r1 = Rectangle(1, 2)
        kwargs = float('Inf')
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_negative_Inf(self):
        r1 = Rectangle(1, 2)
        kwargs = float('-Inf')
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_NaN(self):
        r1 = Rectangle(1, 2)
        kwargs = float('NaN')
        with self.assertRaises(TypeError):
            r1.create(**kwargs)

    def test_no_args(self):
        r1 = Rectangle(1, 2)
        r2 = r1.create()
        self.assertIsInstance(r2, Rectangle)

    def test_more_args(self):
        r1 = Rectangle(1, 2)
        d1 = {"id": 2}
        d2 = {"age": 2}
        with self.assertRaises(TypeError):
            r1.create(d1, d2)


class TestRectangle_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file(cls)'
        class method of Rectangle class

    """

    @classmethod
    def setUp(self):
        """ Create file if it doesn't exist """
        try:
            Rectangle.save_to_file([Rectangle(1, 2)])
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ Delete any created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_output_type(self):
        b = Rectangle.load_from_file()
        self.assertIsInstance(b, list)

    def test_no_args(self):
        b = Rectangle.load_from_file()
        self.assertIsNotNone(b)
        self.assertIsInstance(b, list)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], 1)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(False)

    def test_file_exists(self):
        r1 = Rectangle.load_from_file()
        self.assertIsInstance(r1, list)
        self.assertEqual(r1[0].__class__.__name__, 'Rectangle')

    def test_file_not_found(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()


if __name__ == "__main__":
    unittest.main()
