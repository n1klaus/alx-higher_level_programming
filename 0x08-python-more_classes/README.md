* `0-rectangle.py` - empty `class Rectangle` that defines a rectangle

* `1-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 0-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`

* `2-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 1-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter

* `3-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 2-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`

* `4-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 3-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

* `5-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 4-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`\
> Print the message **Bye rectangle...** when an instance of Rectangle is deleted

* `6-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 5-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`\
> Print the message **Bye rectangle...** when an instance of Rectangle is deleted\
> Public class attribute `number_of_instances`\
    > Initialized to 0\
    > Incremented during each new instance instantiation\
    > Decremented during each instance deletion

* `7-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 6-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`\
> Print the message **Bye rectangle...** when an instance of Rectangle is deleted\
> Public class attribute `number_of_instances`\
    > Initialized to 0\
    > Incremented during each new instance instantiation\
    > Decremented during each instance deletion\
> Public class attribute print_symbol:\
    > Initialized to `#`\
    > Used as symbol for string representation

* `7-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 6-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character '#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`\
> Print the message **Bye rectangle...** when an instance of Rectangle is deleted\
> Public class attribute `number_of_instances`\
    > Initialized to 0\
    > Incremented during each new instance instantiation\
    > Decremented during each instance deletion\
> Public class attribute print_symbol:\
    > Initialized to `#`\
    > Used as symbol for string representation\
> Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area\
    > `rect_1` must be an instance of `Rectangle`\
    > `rect_2` must be an instance of `Rectangle`\
    > Returns `rect_1` if both have the same area value

* `8-rectangle.py` - `class Rectangle` that defines a rectangle by: (based on 7-rectangle.py)
> Private instance attribute: `width`\
    > property `def width(self):` to retrieve it\
    > property setter `def width(self, value):` to set it\
> Private instance attribute: `height`\
    > property `def height(self):` to retrieve it\
    > property setter `def height(self, value)` to set it\
> Instantiation with optional width and height: `def __init__(self, width=0, height=0):`\
> Public instance method: `def area(self):` that returns the rectangle area\
> Public instance method: `def perimeter(self):` that returns the rectangle perimeter\
> print() and str() should print the rectangle with the character `#`\
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`\
> Print the message **Bye rectangle...** when an instance of Rectangle is deleted\
> Public class attribute `number_of_instances`\
    > Initialized to 0\
    > Incremented during each new instance instantiation\
    > Decremented during each instance deletion\
> Public class attribute print_symbol:\
    > Initialized to `#`\
    > Used as symbol for string representation\
> Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area\
    > `rect_1` must be an instance of `Rectangle`\
    > `rect_2` must be an instance of `Rectangle`\
    > Returns `rect_1` if both have the same area value\
> Class method `def square(cls, size=0):` that returns a new `Rectangle` instance with **width == height == size**

`101-nqueens.py` - solves the N queens problem: N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
