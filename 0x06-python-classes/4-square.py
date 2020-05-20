 #!/usr/bin/python3
"""Creates square"""


class Square:
    """The Class"""

    def __init__(self, size=0):
        """Function that initializes atribute for the zise of the square"""
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = size
        except TypeError:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """The size"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """defines square size"""
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = value
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """square area"""
        return (self._Square__size ** 2)
