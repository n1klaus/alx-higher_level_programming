#!/usr/bin/python3
""" Module to define a square class """


class Square():
    """Class definition for a square of given size



    Attributes:
        __size (int): size of the length of the new instance

    """

    def __init__(self, size=0, position=(0, 0)):
        """ The constructor to initialize new square objects

        Args:
            size (:obj:'int', optional): size of the length
            position (:obj:tuple of 'int', optional): size of the length

        """
        try:
            if size >= 0 and isinstance(size, int):
                self.__size = size
        except TypeError:
            print("size must be an integer".format())
        except ValueError:
            print("size must be >= 0".format())
        except Exception:
            raise

        try:
            if isinstance(position, tuple) and\
                    isinstance(position[0], int) and position[0] >= 0 and\
                    isinstance(position[1], int) and position[1] >= 0:
                self.__position = position
        except TypeError:
            print("position must be a tuple of 2 positive integers".format())

    @property
    def size(self):
        """Getter method to retrieve private size attribute

        Returns:
            size of the length

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to change private size attribute

        Args:
            value (int): size of the length

        """
        try:
            if value >= 0 and value is isinstance(value, int):
                self.__size = value
        except TypeError:
            print("size must be an integer".format())
        except ValueError:
            print("size must be >= 0".format())
        except Exception:
            raise

    @property
    def position(self):
        """Getter method to retrieve private position attribute

        Returns:
            obj: int: position of the square for the instance.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to change private position attribute

        Args:
            value (int): position of the square

        Returns:
            obj: int: position of the square

        """
        try:
            if isinstance(value, tuple) and\
                    isinstance(value[0], int) and value[0] >= 0 and\
                    isinstance(value[1], int) and value[1] >= 0:
                self.__position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers".format())
        except Exception:
            raise

    def area(self):
        """Method to calculate the area of the square

        Returns:
            int: area of the square

        """
        return self.__size ** 2

    def my_print(self):
        """Method to print a square with # """
        if self.__size == 0:
            print("".format())
        for r in range(self.__size):
            if self.__position[0] > 0:
                for p in range(self.__position[0]):
                    print(" ".format(p), end="")
            for c in range(self.__size):
                print("#".format(c), end="")
            print("".format(r))
