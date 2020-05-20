#!/usr/bin/python3
"""Creates square"""


class Square:
    """The Class"""

    def __init__(self, size=0):
        """Function that initializes atribute for the zise of the square"""
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
    
    @property
    def size(self):
        """The size"""
        return self.__size


    @size.setter
    def size(self, value):
        """defines square size"""
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """square area"""
        return self.__size ** 2
