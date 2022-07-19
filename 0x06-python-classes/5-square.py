#!/usr/bin/python3
class Square():
    """Class definition for a square.

    Args:
        size (:obj:'int', optional): size of the length

    Attributes:
        __size (int): size of the length of the new instance

    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve private attributes of the instance.

        Args:
            None

        Returns:
            size of the length of the instance.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to change private attributes of the instance.

        Args:
            value (int): size of the length of the new instance

        Returns:
            size of the length of the instance.

        """
        try:
            if value >= 0 and isinstance(value, int):
                self.size = value
        except TypeError:
            print("size must be an integer".format())
        except ValueError:
            print("size must be >= 0".format())
        except Exception:
            raise

    def area(self):
        """Method to calculate the area of the square for the instance.

        Args:
            None

        Returns:
            area of the square for the instance.

        """
        return self.__size ** 2

    def my_print(self):
        """Method to calculate the area of the square for the instance.

        Args:
            None

        Returns:
            area of the square for the instance.

        """
        if self.__size == 0:
            print("".format())
        for r in range(self.__size):
            for c in range(self.__size):
                if c == self.__size - 1:
                    print("#".format(c))
                    break
                print("#".format(r), end="")
