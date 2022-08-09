#!/usr/bin/python3
""" Defines unittests for Square.py """
import unittest
from models.square import Square


class TestSquare__init__(unittest.TestCase):
    """ Unittests for testing the constructor of the Square class
        public method '__init__(self, size, x=0, y=0, id=None)'

        Note:
            Only 1 positional arguments is required, other 3 are optional

    """

    def test_ID_automatic_assignment(self):
        s1 = Square(10)
        s2 = Square(2)
        self.assertGreater(s2.id, s1.id)

    def test_None(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_list(self):
        with self.assertRaises(TypeError):
            Square([1, 2, 3])

    def test_bool_true(self):
        s1 = Square(True)
        self.assertIsInstance(s1, Square)

    def test_bool_false(self):
        with self.assertRaises(ValueError):
            Square(False)

    def test_positive_number(self):
        s1 = Square(4)
        self.assertIsInstance(s1, Square)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            Square(-4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Square(4.99999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Square(complex(5))

    def test_str(self):
        with self.assertRaises(TypeError):
            Square("4")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            Square(("4", 4))

    def test_dict(self):
        with self.assertRaises(TypeError):
            Square({"id": 4})

    def test_set(self):
        with self.assertRaises(TypeError):
            Square({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(TypeError):
            Square(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(TypeError):
            Square(range(5))

    def test_bytes(self):
        with self.assertRaises(TypeError):
            Square(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(TypeError):
            Square(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(TypeError):
            Square(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(TypeError):
            Square(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(TypeError):
            Square(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(TypeError):
            Square(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args(self):
        s1 = Square(1, 12)
        self.assertIsInstance(s1, Square)

    def test_three_args(self):
        s1 = Square(1, 12, 4)
        self.assertIsInstance(s1, Square)

    def test_four_args(self):
        s1 = Square(1, 12, 4, 5)
        self.assertIsInstance(s1, Square)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 12, 4, 5, 6, 7, 8)


class TestSquare_size_setter(unittest.TestCase):
    """ Unittests for testing 'size(self, value)'
        public setter method of the Square class

    """

    def test_no_value_assignment(self):
        s1 = Square(8)
        self.assertIsInstance(s1.size, int)
        self.assertEqual(s1.size, 8)

    def test_more_value_assignment(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = 1, 2, 3

    def test_None(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = None

    def test_list(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = [1, 2, 3]

    def test_bool_true(self):
        s1 = Square(8)
        s1.size = True
        self.assertIsInstance(s1.size, int)
        self.assertTrue(s1.size)

    def test_bool_false(self):
        s1 = Square(8)
        with self.assertRaises(ValueError):
            s1.size = False

    def test_positive_number(self):
        s1 = Square(8)
        s1.size = 4
        self.assertIsInstance(s1.size, int)
        self.assertEqual(s1.size, 4)

    def test_negative_number(self):
        s1 = Square(8)
        with self.assertRaises(ValueError):
            s1.size = -4

    def test_float(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = 4.99999

    def test_complex(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = complex(5)

    def test_str(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = "4"

    def test_tuple(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = (4, 4)

    def test_dict(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = {"id": 4}

    def test_set(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = {12, 24, 36}

    def test_frozenset(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = frozenset({12, 24, 36})

    def test_range(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = range(10)

    def test_bytes(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = b'AtoZ'

    def test_bytearray(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = bytearray(b'AtoZ')

    def test_memoryview(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = memoryview(b'AtoZ')

    def test_Inf(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = float('Inf')

    def test_negative_Inf(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = float('-Inf')

    def test_NaN(self):
        s1 = Square(8)
        with self.assertRaises(TypeError):
            s1.size = float('NaN')


class TestSquare__str__(unittest.TestCase):
    """ Unittests for testing '__str__(self)'
        public method of Square class

    """

    @classmethod
    def setUp(self):
        """ Create Square instance """
        s1 = Square(8, 2, 1, 55)
        self.__str__ = s1.__str__

    def test_output_type(self):
        s = self.__str__()
        self.assertIsNotNone(s)
        self.assertIsInstance(s, str)

    def test_no_args(self):
        s = self.__str__()
        self.assertEqual(s, "[Square] (55) 2/1 - 8")

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


class TestSquare_update(unittest.TestCase):
    """ Unittests for testing 'update(self, *args, **kwargs)'
        public method of Square class

    """

    def test_output_type(self):
        s1 = Square(8, 19, 32, 55)
        args = [1, 2, 3, 4]
        ar = s1.update(*args)
        self.assertIsNone(ar)

    def test_None(self):
        s1 = Square(8, 1, 3, 55)
        args = None
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_list(self):
        s1 = Square(8, 19, 32, 55)
        args = [1, 2, 3, 4]
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

    def test_bool_true(self):
        s1 = Square(8, 1, 3, 55)
        args = True
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_bool_false(self):
        s1 = Square(8, 1, 3, 55)
        args = False
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_positive_number(self):
        s1 = Square(8, 1, 3, 55)
        args = 4
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_negative_number(self):
        s1 = Square(8, 1, 3, 55)
        args = -4
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_float(self):
        s1 = Square(8, 1, 3, 55)
        args = 4.99999
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_complex(self):
        s1 = Square(8, 1, 3, 55)
        args = complex(5)
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_str(self):
        s1 = Square(8, 1, 3, 55)
        args = "4"
        with self.assertRaises(AssertionError):
            s1.update(*args)

    def test_tuple(self):
        s1 = Square(8, 1, 3, 55)
        args = (1, 2, 3, 4)
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

    def test_dict(self):
        s1 = Square(8, 1, 3, 55)
        kwargs = {"id": 1, "size": 3, "x": 4, "y": 5}
        s1.update(**kwargs)
        self.assertEqual(s1.__str__(), '[Square] (1) 4/5 - 3')

    def test_set(self):
        s1 = Square(8, 1, 3, 55)
        args = {1, 2, 3, 4, 5}
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

    def test_frozenset(self):
        s1 = Square(8, 1, 3, 55)
        args = frozenset({1, 2, 3, 4, 5})
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

    def test_range(self):
        s1 = Square(8, 1, 3, 55)
        args = range(4)
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (0) 2/3 - 1')

    def test_bytes(self):
        s1 = Square(8, 1, 3, 55)
        args = b'AtoZ'
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (65) 111/90 - 116')

    def test_bytearray(self):
        s1 = Square(8, 1, 3, 55)
        args = bytearray(b'AtoZ')
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (65) 111/90 - 116')

    def test_memoryview(self):
        s1 = Square(8, 1, 3, 55)
        args = memoryview(b'AtoZ')
        s1.update(*args)
        self.assertEqual(s1.__str__(), '[Square] (65) 111/90 - 116')

    def test_Inf(self):
        s1 = Square(8, 1, 3, 55)
        args = float('Inf')
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_negative_Inf(self):
        s1 = Square(8, 1, 3, 55)
        args = float('-Inf')
        with self.assertRaises(TypeError):
            s1.update(*args)

    def test_NaN(self):
        s1 = Square(8, 1, 3, 55)
        args = float('NaN')
        with self.assertRaises(TypeError):
            s1.update(*args)


class TestSquare_to_dictionary(unittest.TestCase):
    """ Unittests for testing 'to_dictionary(self)'
        public method of Square class

    """

    @classmethod
    def setUp(self):
        """ Create Square instance """
        s1 = Square(8, 1, 3, 55)
        self.to_dictionary = s1.to_dictionary

    def test_output_type(self):
        d = self.to_dictionary()
        self.assertIsInstance(d, dict)

    def test_no_args(self):
        d = self.to_dictionary()
        self.assertIsNotNone(d)
        self.assertDictEqual(d,
                             {
                                'id': 55,
                                'size': 8,
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
