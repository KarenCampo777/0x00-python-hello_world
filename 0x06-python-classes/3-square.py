#!/usr/bin/python3
"""Creates a square"""


class Square:
    """The Class"""
    def __init__(self, size=0):
        """Initializes data"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns square area"""
        return self.__size ** 2
