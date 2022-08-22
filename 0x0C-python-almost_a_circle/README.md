# Unittest on Inheritance

#### Base Geometry Class
1. [Class Base](models/base.py) => [Unittest for Class Base](tests/test_models/test_base.py)

> ***`class Base`***
>
>*  private class attribute `__nb_objects`
>* class constructor: `def __init__(self, id=None):`
>* static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`
>* class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file
>* static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`
>* class method `def create(cls, **dictionary):` that returns an instance with all attributes already set
>* class method `def load_from_file(cls):` that returns a list of instances


#### Rectangle Class
2. [Class Rectangle](models/rectangle.py) => [Unittest for Class Rectangle](tests/test_models/test_rectangle.py)

> ***`class Rectangle`*** that inherits from ***`class Base`***
>
>* Private instance attributes, each with its own public getter and setter: `__width` -> `width`, `__height` -> `height`, `__x` -> `x`, `__y` -> `y`
>* Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`
>* public method `def area(self):` that returns the area value of the Rectangle instance.
>* public method `def display(self):` that prints in stdout the Rectangle instance with the character `#`
>* overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
>* public method `def display(self):` to print in stdout the Rectangle instance with the character `#` by taking care of `x` and `y`
>* public method `update(self, *args, **kwargs)` that assigns an argument to each attribute
>* public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle:


#### Square Class
3. [Class Square](models/square.py) => [Unittest for Class Square](tests/test_models/test_square.py)

> `class Square` that inherits from `class Rectangle`
>
>* Class constructor:   `def __init__(self, size, x=0, y=0, id=None):`
>* overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>`
>* public getter and setter `size`
>* public method `def update(self, *args, **kwargs)` that assigns attributes
>* public method `def to_dictionary(self):` that returns the dictionary representation of a Square
