#!/usr/bin/python3
""" Defines unittests for Square.py """
import unittest
import json
import os
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

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_positive_number(self):
        s1 = Square(4)
        self.assertIsInstance(s1, Square)

    def test_negative_number_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_number_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_number_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_negative_number_id(self):
        with self.assertRaises(AssertionError):
            Square(1, 2, 3, -4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Square(4.99999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Square(complex(5))

    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_str_id(self):
        with self.assertRaises(AssertionError):
            Square(1, 2, 3, "4")

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

    def test_output_type(self):
        s = Square(8, 2, 1, 55).__str__()
        self.assertIsNotNone(s)
        self.assertIsInstance(s, str)

    def test_no_args(self):
        s = Square(8, 2, 1, 55).__str__()
        self.assertEqual(s, "[Square] (55) 2/1 - 8")

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Square(8, 2, 1, 55).__str__(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Square(8, 2, 1, 55).__str__(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Square(8, 2, 1, 55).__str__(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Square(8, 2, 1, 55).__str__(False)


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

    def test_insert_number_id(self):
        s1 = Square(8, 1, 3, 55).update(89)
        self.assertEqual(s1.__str__(), 'None')

    def test_insert_number_size(self):
        s1 = Square(8, 1, 3, 55).update(89, 1)
        self.assertEqual(s1.__str__(), 'None')

    def test_insert_number_x(self):
        s1 = Square(8, 1, 3, 55).update(89, 1, 2, 3)
        self.assertEqual(s1.__str__(), 'None')

    def test_insert_number_y(self):
        s1 = Square(8, 1, 3, 55).update(89, 1, 2, 3, 4)
        self.assertEqual(s1.__str__(), 'None')

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

    def test_dict_id(self):
        s1 = Square(8, 1, 3, 55)
        kwargs = {"id": 1}
        s1.update(**kwargs)
        self.assertEqual(s1.__str__(), '[Square] (1) 1/3 - 8')

    def test_dict_size(self):
        s1 = Square(8, 1, 3, 55)
        kwargs = {"id": 1, "size": 3}
        s1.update(**kwargs)
        self.assertEqual(s1.__str__(), '[Square] (1) 1/3 - 3')

    def test_dict_x(self):
        s1 = Square(8, 1, 3, 55)
        kwargs = {"id": 1, "size": 3, "x": 4}
        s1.update(**kwargs)
        self.assertEqual(s1.__str__(), '[Square] (1) 4/3 - 3')

    def test_dict_y(self):
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

    def test_no_args(self):
        s1 = Square(8, 1, 3, 55)
        s1.update()
        self.assertEqual(s1.__str__(), '[Square] (55) 1/3 - 8')


class TestSquare_to_dictionary(unittest.TestCase):
    """ Unittests for testing 'to_dictionary(self)'
        public method of Square class

    """

    def test_output_type(self):
        d = Square(8, 1, 3, 55).to_dictionary()
        self.assertIsInstance(d, dict)

    def test_no_args(self):
        d = Square(8, 1, 3, 55).to_dictionary()
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
            Square(8, 1, 3, 55).to_dictionary(3, 4)

    def test_None(self):
        with self.assertRaises(TypeError):
            Square(8, 1, 3, 55).to_dictionary(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Square(8, 1, 3, 55).to_dictionary(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Square(8, 1, 3, 55).to_dictionary(False)


class TestSquare_to_json_string(unittest.TestCase):
    """ Unittests for testing 'to_json_string(list_dictionaries)'
        static method of the Square class

    """

    def test_empty_list(self):
        self.assertEqual("[]", Square.to_json_string([]))

    def test__None(self):
        self.assertEqual("[]", Square.to_json_string(None))

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(True)

    def test_bool_false(self):
        self.assertEqual("[]", Square.to_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Square.to_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.to_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Square.to_json_string([], [])


class TestSquare_save_to_file(unittest.TestCase):
    """ Unittests for testing 'save_to_file(cls, list_objs)'
        class method of Square class

    """

    @classmethod
    def tearDown(self):
        """ Delete created files """
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_create_new_file(self):
        s1 = Square(12, 1, 1, 9)
        Square.save_to_file([s1])
        stream = str()
        with open("Square.json", "r") as f:
            stream += f.read()
        res = json.loads(stream)
        self.assertEqual(res[0].get('id'), 9)
        self.assertEqual(res[0].get('_Rectangle__width'), 12)
        self.assertEqual(res[0].get('_Rectangle__height'), 12)
        self.assertEqual(res[0].get('_Rectangle__x'), 1)
        self.assertEqual(res[0].get('_Rectangle__y'), 1)

    def test_overwrite_file(self):
        s1 = Square(24, 11, 23, 98)
        s2 = Square(36, 45, 13, 48)
        Square.save_to_file([s1])
        stream1 = str()
        with open("Square.json", "r") as f1:
            stream1 += f1.read()
        res = json.loads(stream1)
        self.assertEqual(res[0].get('id'), 98)
        self.assertEqual(res[0].get('_Rectangle__width'), 24)
        self.assertEqual(res[0].get('_Rectangle__height'), 24)
        self.assertEqual(res[0].get('_Rectangle__x'), 11)
        self.assertEqual(res[0].get('_Rectangle__y'), 23)
        Square.save_to_file([s2])
        stream2 = str()
        with open("Square.json", "r") as f2:
            stream2 += f2.read()
        res = json.loads(stream2)
        self.assertEqual(res[0].get('id'), 48)
        self.assertEqual(res[0].get('_Rectangle__width'), 36)
        self.assertEqual(res[0].get('_Rectangle__height'), 36)
        self.assertEqual(res[0].get('_Rectangle__x'), 45)
        self.assertEqual(res[0].get('_Rectangle__y'), 13)

    def test_None(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(None)

    def test_empty_list(self):
        Square.save_to_file([])
        stream = str()
        with open("Square.json", "r") as f:
            stream += f.read()
        self.assertEqual("[]", stream)

    def test_list_square(self):
        Square.save_to_file([Square(8)])
        stream = str()
        with open("Square.json", "r") as f:
            stream += f.read()
        self.assertEqual(len(str(Square(8).__dict__)) + 2, len(stream))

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(True)

    def test_bool_false(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(False)

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([1], [12])


class TestSquare_from_json_string(unittest.TestCase):
    """ Unittests for testing 'from_json_string(json_string)'
        static method of Square class

    """

    def test_output_type(self):
        list_output = Square.from_json_string('[{"id": 4}]')
        self.assertIsInstance(list_output, list)

    def test_None(self):
        self.assertEqual([], Square.from_json_string(None))

    def test_empty_list(self):
        self.assertEqual([], Square.from_json_string("[]"))

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(True)

    def test_bool_false(self):
        self.assertEqual([], Square.from_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(-4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(TypeError):
            Square.from_json_string("4")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(TypeError):
            Square.from_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(TypeError):
            Square.from_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Square.from_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Square.from_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(TypeError):
            Square.from_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.from_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Square.from_json_string([], 4)


class TestSquare_create(unittest.TestCase):
    """ Unittests for testing 'create(cls, **dictionary)'
        class method of Square class

    """

    def test_None(self):
        s1 = Square(8)
        kwargs = None
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_empty_dictionary(self):
        s1 = Square(8)
        kwargs = {}
        s2 = s1.create(**kwargs)
        self.assertIsInstance(s2, Square)

    def test_dict_id(self):
        s1 = Square(8)
        kwargs = {'id': 89}
        s2 = s1.create(**kwargs)
        self.assertEqual(s2.__dict__.get('id'), kwargs.get('id'))

    def test_dict_size(self):
        s1 = Square(8)
        kwargs = {'id': 89, 'size': 1}
        s2 = s1.create(**kwargs)
        self.assertEqual(s2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(s2.__dict__.get('_Rectangle__width'),
                         kwargs.get('size'))
        self.assertEqual(s2.__dict__.get('_Rectangle__height'),
                         kwargs.get('size'))

    def test_dict_x(self):
        s1 = Square(8)
        kwargs = {'id': 89, 'size': 1, 'x': 2}
        s2 = s1.create(**kwargs)
        self.assertEqual(s2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(s2.__dict__.get('_Rectangle__width'),
                         kwargs.get('size'))
        self.assertEqual(s2.__dict__.get('_Rectangle__height'),
                         kwargs.get('size'))
        self.assertEqual(s2.__dict__.get('_Rectangle__x'), kwargs.get('x'))

    def test_dict_y(self):
        s1 = Square(8)
        kwargs = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s2 = s1.create(**kwargs)
        self.assertEqual(s2.__dict__.get('id'), kwargs.get('id'))
        self.assertEqual(s2.__dict__.get('_Rectangle__width'),
                         kwargs.get('size'))
        self.assertEqual(s2.__dict__.get('_Rectangle__height'),
                         kwargs.get('size'))
        self.assertEqual(s2.__dict__.get('_Rectangle__x'), kwargs.get('x'))
        self.assertEqual(s2.__dict__.get('_Rectangle__y'), kwargs.get('y'))

    def test_bool_true(self):
        s1 = Square(8)
        kwargs = True
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_bool_false(self):
        s1 = Square(8)
        kwargs = False
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_positive_number(self):
        s1 = Square(8)
        kwargs = 4
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_negative_number(self):
        s1 = Square(8)
        kwargs = -4
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_float(self):
        s1 = Square(8)
        kwargs = 4.99999
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_complex(self):
        s1 = Square(8)
        kwargs = complex(5)
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_str(self):
        s1 = Square(8)
        kwargs = "4"
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_tuple(self):
        s1 = Square(8)
        kwargs = ("4", 4)
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_set(self):
        s1 = Square(8)
        kwargs = {12, 24, 36}
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_frozenset(self):
        s1 = Square(8)
        kwargs = frozenset({12, 24, 36})
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_range(self):
        s1 = Square(8)
        kwargs = range(5)
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_bytes(self):
        s1 = Square(8)
        kwargs = b'AtoZ'
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_bytearray(self):
        s1 = Square(8)
        kwargs = bytearray(b'AtoZ')
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_memoryview(self):
        s1 = Square(8)
        kwargs = memoryview(b'AtoZ')
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_Inf(self):
        s1 = Square(8)
        kwargs = float('Inf')
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_negative_Inf(self):
        s1 = Square(8)
        kwargs = float('-Inf')
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_NaN(self):
        s1 = Square(8)
        kwargs = float('NaN')
        with self.assertRaises(TypeError):
            s1.create(**kwargs)

    def test_no_args(self):
        s1 = Square(8)
        s2 = s1.create()
        self.assertIsInstance(s2, Square)

    def test_more_args(self):
        s1 = Square(8)
        d1 = {"id": 2}
        d2 = {"age": 2}
        with self.assertRaises(TypeError):
            s1.create(d1, d2)


class TestSquare_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file(cls)'
        class method of Square class

    """

    @classmethod
    def setUp(self):
        """ Create file if it doesn't exist """
        try:
            Square.save_to_file([Square(1)])
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ Delete any created files """
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_output_type(self):
        b = Square.load_from_file()
        self.assertIsInstance(b, list)

    def test_no_args(self):
        b = Square.load_from_file()
        self.assertIsNotNone(b)
        self.assertIsInstance(b, list)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Square.load_from_file([], 1)

    def test_None(self):
        with self.assertRaises(TypeError):
            Square.load_from_file(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Square.load_from_file(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Square.load_from_file(False)

    def test_file_exists(self):
        s1 = Square.load_from_file()
        self.assertIsInstance(s1, list)
        self.assertEqual(s1[0].__class__.__name__, 'Square')

    def test_file_not_found(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass
        with self.assertRaises(FileNotFoundError):
            Square.load_from_file()


if __name__ == "__main__":
    unittest.main()
