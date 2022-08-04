`0-lookup.py` - function that returns the list of available attributes and methods of an object

`1-my_list.py` - `class MyList` that inherits from `list`\
> tests/1-my_list.txt - doctest testfile for `1-my_list.py`

`2-is_same_class.py` -  function that returns True if the object is exactly an instance of the specified class; otherwise False.

`3-is_kind_of_class.py` - function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

`4-inherits_from.py` -  function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False

`5-base_geometry.py` - empty `class BaseGeometry`

`6-base_geometry.py` - `class BaseGeometry` (based on `5-base_geometry.py`)\
> Public instance method: `def area(self):` that raises an Exception with the message ***area() is not implemented***

`7-base_geometry.py` - `class BaseGeometry` (based on `6-base_geometry.py`)\
    > Public instance method: `def area(self):` that raises an Exception with the message ***area() is not implemented***\
    > Public instance method: `def integer_validator(self, name, value):` that validates value\
> tests/7-base_geometry.txt - doctest testfile for `7-base_geometry.py`

`8-rectangle.py` - `class Rectangle` that inherits from BaseGeometry (`7-base_geometry.py`)\
> Instantiation with `width` and `height`: `def __init__(self, width, height):`

`9-rectangle.py` - `class Rectangle` that inherits from BaseGeometry (`8-base_geometry.py`)\
> Instantiation with `width` and `height`: `def __init__(self, width, height):`\
> the `area()` method must be implemented\
> `print()` should print, and `str()` should return, the following rectangle description: ***[Rectangle] <width>/<height>***

`10-square.py` - `class Square` that inherits from Rectangle (`9-rectangle.py`)\
> Instantiation with size: `def __init__(self, size):`\
> the `area()` method must be implemented

`11-square.py` - `class Square` that inherits from Rectangle (`10-square.py`)\
> Instantiation with size: `def __init__(self, size):`\
> the `area()` method must be implemented\
> `print()` should print, and `str()` should return, the square description: ***[Square] <width>/<height>***

`100-my_int.py` -  `class MyInt` that inherits from `int`\
> MyInt has `==` and `!=` operators inverted

`101-add_attribute.py` - function that adds a new attribute to an object if it’s possible
