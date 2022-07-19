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
    def _size(self):
        """Getter method to retrieve private attributes of the instance.

        Args:
            None

        Returns:
            size of the length of the instance.

        """
        return self.__size

    @_size.setter
    def _size(self, size):
        """Setter method to change private attributes of the instance.

        Args:
            size (:obj:'int'): size of the length of the new instance

        Returns:
            size of the length of the instance.

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
        finally:
            return self.__size

    def area(self):
        """Method to calculate the area of the square for the instance.

        Args:
            None

        Returns:
            area of the square for the instance.

        """
        return self.__size ** 2
