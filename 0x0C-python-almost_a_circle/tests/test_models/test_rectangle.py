#!/usr/bin/python3
""" Defines unittests for rectangle.py """
import unittest
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

    def test_positive_number(self):
        r1 = Rectangle(4, 4)
        self.assertIsInstance(r1, Rectangle)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, -4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(4.99999, 4.99999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Rectangle(complex(5), complex(5))

    def test_str(self):
        with self.assertRaises(TypeError):
            Rectangle("4", "4")

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
        r1 = Rectangle(1, 12, 4)
        self.assertIsInstance(r1, Rectangle)

    def test_four_args(self):
        r1 = Rectangle(1, 12, 4, 5)
        self.assertIsInstance(r1, Rectangle)

    def test_five_args(self):
        r1 = Rectangle(1, 12, 4, 5, 6)
        self.assertIsInstance(r1, Rectangle)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 12, 4, 5, 6, 7, 8)


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

    @classmethod
    def setUp(self):
        """ Create Rectangle instance """
        r1 = Rectangle(8, 4, 1, 3)
        self.area = r1.area

    def test_output_type(self):
        a = self.area()
        self.assertIsInstance(a, int)

    def test_no_args(self):
        a = self.area()
        self.assertEqual(a, 32)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.area(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            self.area(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            self.area(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            self.area(False)


class TestRectangle_display(unittest.TestCase):
    """ Unittests for testing 'display(self)'
        public method of Rectangle class

    """

    @classmethod
    def setUp(self):
        """ Create Rectangle instance """
        r1 = Rectangle(8, 4, 1, 3)
        self.display = r1.display

    def test_output_type(self):
        d = self.display()
        self.assertIsNone(d)

    def test_no_x_and_no_y(self):
        r2 = Rectangle(8, 4)
        d = r2.display()
        self.assertIsNone(d)
        self.assertIsInstance(r2, Rectangle)

    def test_no_args(self):
        d = self.display()
        self.assertIsNone(d)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.display(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            self.display(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            self.display(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            self.display(False)


class TestRectangle__str__(unittest.TestCase):
    """ Unittests for testing '__str__(self)'
        public method of Rectangle class

    """

    @classmethod
    def setUp(self):
        """ Create Rectangle instance """
        r1 = Rectangle(8, 4, 1, 3, 55)
        self.__str__ = r1.__str__

    def test_output_type(self):
        s = self.__str__()
        self.assertIsNotNone(s)
        self.assertIsInstance(s, str)

    def test_no_args(self):
        s = self.__str__()
        self.assertEqual(s, "[Rectangle] (55) 1/3 - 8/4")

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.__str__(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            self.__str__(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            self.__str__(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            self.__str__(False)


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

    def test_dict(self):
        r1 = Rectangle(8, 4, 1, 3, 55)
        kwargs = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        r1.update(**kwargs)
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


class TestRectangle_to_dictionary(unittest.TestCase):
    """ Unittests for testing 'to_dictionary(self)'
        public method of Rectangle class

    """
    @classmethod
    def setUp(self):
        """ Create Rectangle instance """
        r1 = Rectangle(8, 4, 1, 3, 55)
        self.to_dictionary = r1.to_dictionary

    def test_output_type(self):
        d = self.to_dictionary()
        self.assertIsInstance(d, dict)

    def test_no_args(self):
        d = self.to_dictionary()
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
            self.to_dictionary(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            self.to_dictionary(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            self.to_dictionary(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            self.to_dictionary(False)


if __name__ == "__main__":
    unittest.main()
