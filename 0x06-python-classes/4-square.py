#!/usr/bin/python3
""" Module to define a square class """


class Square():
    """Class definition for a square of given size

    Attributes:
        __size (int): size of the length

    """

    def __init__(self, size=0):
        """ The constructor to initialize new square objects

        Args:
            size (:obj:'int'): size of the length

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

    @property
    def _size(self):
        """Getter method to retrieve private attributes

        Returns:
            int: size of the length

        """
        return self.__size

    @_size.setter
    def _size(self, value):
        """Setter method to change private attributes

        Args:
            value (int): size of the length

        """
        try:
            if value >= 0 and isinstance(value, int):
                self.__size = value
        except TypeError:
            print("size must be an integer".format())
        except ValueError:
            print("size must be >= 0".format())
        except Exception:
            raise

    def area(self):
        """Method to calculate the area of the square

        Returns:
            int: area of the square

        """
        return self.__size ** 2
