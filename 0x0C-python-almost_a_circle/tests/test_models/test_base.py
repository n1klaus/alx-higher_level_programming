#!/usr/bin/python3
""" Defines unittests for base.py """
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase__init__(unittest.TestCase):
    """ Unittests for testing the constructor of the Base class
        public method '__init__(self, id=None)'

    """

    def test_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertIsInstance(b1, Base)

    def test_consecutive_automatic_assignment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base()
        self.assertGreater(b2.id, b1.id)
        self.assertGreater(b4.id, b2.id)
        self.assertGreater(b4.id, b1.id)
        self.assertGreater(b5.id, b4.id)
        self.assertGreater(b5.id, b2.id)
        self.assertGreater(b5.id, b1.id)
        self.assertGreater(b3.id, b5.id)
        self.assertGreater(b3.id, b4.id)
        self.assertGreater(b3.id, b2.id)
        self.assertGreater(b3.id, b1.id)

    def test_output_type(self):
        b1 = Base()
        self.assertIsInstance(b1.id, int)
        self.assertIsInstance(b1, Base)

    def test_no_args(self):
        b1 = Base()
        self.assertGreater(b1.id, 1)
        self.assertIsInstance(b1, Base)

    def test_single_automatic_assignment(self):
        b1 = Base(12)
        b2 = Base()
        self.assertGreater(b1.id, b2.id)

    def test_positive_integer(self):
        self.assertEqual(12, Base(12).id)

    def test_negative_integer(self):
        with self.assertRaises(AssertionError):
            Base(-12).id

    def test_float(self):
        with self.assertRaises(AssertionError):
            Base(12.99999).id

    def test_nb_instances_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str(self):
        with self.assertRaises(AssertionError):
            Base("12").id

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Base(complex(5)).id

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Base({"id": 1, "name": 2}).id

    def test_bool_true(self):
        self.assertTrue(Base(True).id)

    def test_bool_false(self):
        with self.assertRaises(AssertionError):
            Base(False).id

    def test_list(self):
        with self.assertRaises(AssertionError):
            Base([12, 24, 36]).id

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Base((12, 24, 36)).id

    def test_set(self):
        with self.assertRaises(AssertionError):
            Base({12, 24, 36}).id

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Base(frozenset({12, 24, 36})).id

    def test_range(self):
        with self.assertRaises(AssertionError):
            Base(range(5)).id

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Base(b'AtoZ').id

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Base(bytearray(b'AtoZ')).id

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Base(memoryview(b'AtoZ')).id

    def test_inf(self):
        with self.assertRaises(AssertionError):
            Base(float('Inf')).id

    def test_negative_inf(self):
        with self.assertRaises(AssertionError):
            Base(float('-Inf')).id

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Base(float('NaN')).id

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """ Unittests for testing 'to_json_string(list_dictionaries)'
        static method of the Base class

    """

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test__None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(True)

    def test_bool_false(self):
        self.assertEqual("[]", Base.to_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Base.to_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


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


class TestBase_save_to_file(unittest.TestCase):
    """ Unittests for testing 'save_to_file(cls, list_objs)'
        class method of Base class

    """

    # @classmethod
    # def tearDown(self):
    #     """ Delete created files """
    #     try:
    #         os.remove("Base.json")
    #     except IOError:
    #         pass

    def test_create_new_file(self):
        b1 = Base(12)
        Base.save_to_file([b1])
        stream = str()
        with open("Base.json", "r") as f:
            stream += f.read()
        self.assertEqual(stream, '[{"id": 12}]')

    def test_overwrite_file(self):
        b1 = Base(24)
        b2 = Base(36)
        Base.save_to_file([b1])
        stream1 = str()
        with open("Base.json", "r") as f1:
            stream1 += f1.read()
        self.assertEqual(stream1, '[{"id": 24}]')
        Base.save_to_file([b2])
        stream2 = str()
        with open("Base.json", "r") as f2:
            stream2 += f2.read()
        self.assertEqual(stream2, '[{"id": 36}]')

    def test_None(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(None)

    def test_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_bool_true(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(True)

    def test_bool_false(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(False)

    def test_positive_number(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(4)

    def test_negative_number(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(-4)

    def test_float(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(4.9999)

    def test_complex(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(complex(5))

    def test_str(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file("4")

    def test_tuple(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(("4", 4))

    def test_dict(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file({"id": 4})

    def test_set(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(range(5))

    def test_bytes(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(AssertionError):
            Base.save_to_file(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([1], [12])


class TestRectangle_save_to_file(unittest.TestCase):
    """ Unittests for testing 'save_to_file(cls, list_objs)'
        class method for Rectangle class

    """

    # @classmethod
    # def tearDown(self):
    #     """ Delete created files """
    #     try:
    #         os.remove("Rectangle.json")
    #     except IOError:
    #         pass

    def test_create_new_file(self):
        r1 = Rectangle(12, 20, 1, 1, 19)
        Rectangle.save_to_file([r1])
        stream = str()
        with open("Rectangle.json", "r") as f:
            stream += f.read()
        self.assertEqual(stream, '[{"id": 19, "_Rectangle__width": 12, "_Rectangle__height": 20, "_Rectangle__x": 1, "_Rectangle__y": 1}]')

    def test_overwrite_file(self):
        r1 = Rectangle(24, 30, 2, 3, 11)
        r2 = Rectangle(36, 40, 5, 6, 8)
        Rectangle.save_to_file([r1])
        stream1 = str()
        with open("Rectangle.json", "r") as f1:
            stream1 += f1.read()
        self.assertEqual(stream1, '[{"id": 11, "_Rectangle__width": 24, "_Rectangle__height": 30, "_Rectangle__x": 2, "_Rectangle__y": 3}]')
        Rectangle.save_to_file([r2])
        stream2 = str()
        with open("Rectangle.json", "r") as f2:
            stream2 += f2.read()
        self.assertEqual(stream2, '[{"id": 8, "_Rectangle__width": 36, "_Rectangle__height": 40, "_Rectangle__x": 5, "_Rectangle__y": 6}]')

    def test_None(self):
        with self.assertRaises(AssertionError):
            Rectangle.save_to_file(None)

    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

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


class TestSquare_save_to_file(unittest.TestCase):
    """ Unittests for testing 'save_to_file(cls, list_objs)'
        class method of Square class

    """

    # @classmethod
    # def tearDown(self):
    #     """ Delete created files """
    #     try:
    #         os.remove("Square.json")
    #     except IOError:
    #         pass

    def test_create_new_file(self):
        s1 = Square(12, 1, 1, 9)
        Square.save_to_file([s1])
        stream = str()
        with open("Square.json", "r") as f:
            stream += f.read()
        self.assertEqual(stream, '[{"id": 9, "_Rectangle__width": 12, "_Rectangle__height": 12, "_Rectangle__x": 1, "_Rectangle__y": 1}]')

    def test_overwrite_file(self):
        s1 = Square(24, 11, 23, 98)
        s2 = Square(36, 45, 13, 48)
        Square.save_to_file([s1])
        stream1 = str()
        with open("Square.json", "r") as f1:
            stream1 += f1.read()
        self.assertEqual(stream1, '[{"id": 98, "_Rectangle__width": 24, "_Rectangle__height": 24, "_Rectangle__x": 11, "_Rectangle__y": 23}]')
        Square.save_to_file([s2])
        stream2 = str()
        with open("Square.json", "r") as f2:
            stream2 += f2.read()
        self.assertEqual(stream2, '[{"id": 48, "_Rectangle__width": 36, "_Rectangle__height": 36, "_Rectangle__x": 45, "_Rectangle__y": 13}]')

    def test_None(self):
        with self.assertRaises(AssertionError):
            Square.save_to_file(None)

    def test_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

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


class TestBase_from_json_string(unittest.TestCase):
    """ Unittests for testing 'from_json_string(json_string)'
        static method of Base class

    """

    def test_output_type(self):
        list_output = Base.from_json_string('[{"id": 4}]')
        self.assertIsInstance(list_output, list)

    def test_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(True)

    def test_bool_false(self):
        self.assertEqual([], Base.from_json_string(False))

    def test_positive_number(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(4)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(-4)

    def test_float(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(4.9999)

    def test_complex(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(complex(5))

    def test_str(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("4")

    def test_tuple(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(("4", 4))

    def test_dict(self):
        with self.assertRaises(TypeError):
            Base.from_json_string({"id": 4})

    def test_set(self):
        with self.assertRaises(TypeError):
            Base.from_json_string({12, 24, 36})

    def test_frozenset(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(frozenset({12, 24, 36}))

    def test_range(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(range(5))

    def test_bytes(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(b'AtoZ')

    def test_bytearray(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(bytearray(b'AtoZ'))

    def test_memoryview(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(memoryview(b'AtoZ'))

    def test_Inf(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(float('Inf'))

    def test_negative_Inf(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(float('-Inf'))

    def test_NaN(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(float('NaN'))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 4)


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


class TestBase_create(unittest.TestCase):
    """ Unittests for testing 'create(cls, **dictionary)'
        class method of Base class

    """

    def test_None(self):
        d1 = None
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_empty_dictionary(self):
        d1 = {}
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_bool_true(self):
        d1 = True
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_bool_false(self):
        d1 = False
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_positive_number(self):
        d1 = 4
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_negative_number(self):
        d1 = -4
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_float(self):
        d1 = 4.99999
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_complex(self):
        d1 = complex(5)
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_str(self):
        d1 = "4"
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_tuple(self):
        d1 = ("4", 4)
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_set(self):
        d1 = {12, 24, 36}
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_frozenset(self):
        d1 = frozenset({12, 24, 36})
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_range(self):
        d1 = range(5)
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_bytes(self):
        d1 = b'AtoZ'
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_bytearray(self):
        d1 = bytearray(b'AtoZ')
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_memoryview(self):
        d1 = memoryview(b'AtoZ')
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_Inf(self):
        d1 = float('Inf')
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_negative_Inf(self):
        d1 = float('-Inf')
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_NaN(self):
        d1 = float('NaN')
        with self.assertRaises(TypeError):
            Base.create(**d1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.create()

    def test_more_args(self):
        d1 = {"id": 2}
        d2 = {"age": 2}
        with self.assertRaises(TypeError):
            Base.create(d1, d2)


class TestRectangle_create(unittest.TestCase):
    """ Unittests for testing 'create(cls, **dictionary)'
        class method of Rectangle class

    """

    def test_None(self):
        d1 = None
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_empty_dictionary(self):
        d = {}
        with self.assertRaises(TypeError):
            Rectangle.create(**d)

    def test_bool_true(self):
        d1 = True
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_bool_false(self):
        d1 = False
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_positive_number(self):
        d1 = 4
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_negative_number(self):
        d1 = -4
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_float(self):
        d1 = 4.99999
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_complex(self):
        d1 = complex(5)
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_str(self):
        d1 = "4"
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_tuple(self):
        d1 = ("4", 4)
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_set(self):
        d1 = {12, 24, 36}
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_frozenset(self):
        d1 = frozenset({12, 24, 36})
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_range(self):
        d1 = range(5)
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_bytes(self):
        d1 = b'AtoZ'
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_bytearray(self):
        d1 = bytearray(b'AtoZ')
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_memoryview(self):
        d1 = memoryview(b'AtoZ')
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_Inf(self):
        d1 = float('Inf')
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_negative_Inf(self):
        d1 = float('-Inf')
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_NaN(self):
        d1 = float('NaN')
        with self.assertRaises(TypeError):
            Rectangle.create(**d1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.create()

    def test_more_args(self):
        d1 = {"id": 2}
        d2 = {"age": 2}
        with self.assertRaises(TypeError):
            Rectangle.create(d1, d2)


class TestSquare_create(unittest.TestCase):
    """ Unittests for testing 'create(cls, **dictionary)'
        class method of Square class

    """

    def test_None(self):
        d1 = None
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_empty_dictionary(self):
        d1 = {}
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_bool_true(self):
        d1 = True
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_bool_false(self):
        d1 = False
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_positive_number(self):
        d1 = 4
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_negative_number(self):
        d1 = -4
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_float(self):
        d1 = 4.99999
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_complex(self):
        d1 = complex(5)
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_str(self):
        d1 = "4"
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_tuple(self):
        d1 = ("4", 4)
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_set(self):
        d1 = {12, 24, 36}
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_frozenset(self):
        d1 = frozenset({12, 24, 36})
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_range(self):
        d1 = range(5)
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_bytes(self):
        d1 = b'AtoZ'
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_bytearray(self):
        d1 = bytearray(b'AtoZ')
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_memoryview(self):
        d1 = memoryview(b'AtoZ')
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_Inf(self):
        d1 = float('Inf')
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_negative_Inf(self):
        d1 = float('-Inf')
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_NaN(self):
        d1 = float('NaN')
        with self.assertRaises(TypeError):
            Square.create(**d1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.create()

    def test_more_args(self):
        d1 = {"id": 2}
        d2 = {"age": 2}
        with self.assertRaises(TypeError):
            Square.create(d1, d2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file(cls)'
        class method of Base class

    """

    @classmethod
    def tearDown(self):
        """ Delete any created files """
        try:
            os.remove("Base.json")
        except IOError:
            pass

    # def test_output_type(self):
    #     b = Base.load_from_file()
    #     self.assertIsInstance(b, list)

    # def test_no_args(self):
    #     b = Base.load_from_file()
    #     self.assertIsNotNone(b)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_None(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(None)

    def test_bool_true(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(True)

    def test_bool_false(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(False)

    def test_file_not_found(self):
        try:
            os.remove("Base.json")
        except IOError:
            pass
        with self.assertRaises(FileNotFoundError):
            Base.load_from_file()


class TestRectangle_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file(cls)'
        class method of Rectangle class

    """

    @classmethod
    def tearDown(self):
        """ Delete any created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    # def test_output_type(self):
    #     b = Rectangle.load_from_file()
    #     self.assertIsInstance(b, list)

    # def test_no_args(self):
    #     b = Rectangle.load_from_file()
    #     self.assertIsNotNone(b)

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

    def test_file_not_found(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()


class TestSquare_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file(cls)'
        class method of Square class

    """

    @classmethod
    def tearDown(self):
        """ Delete any created files """
        try:
            os.remove("Square.json")
        except IOError:
            pass

    # def test_output_type(self):
    #     b = Square.load_from_file()
    #     self.assertIsInstance(b, list)

    # def test_no_args(self):
    #     b = Square.load_from_file()
    #     self.assertIsNotNone(b)

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

    def test_file_not_found(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass
        with self.assertRaises(FileNotFoundError):
            Square.load_from_file()


if __name__ == "__main__":
    unittest.main()
