#!/usr/bin/python3
"""Define or create a square"""


class Square:
        """The Class"""
        def __init__(self, size=0):
                """Initialization"""
                self.__size = size

        def area(self):
                """The square area"""
                return self.__size ** 2

        @property
        def size(self):
                """ The size of the square """
                return self.__size

        @size.setter
        def size(self, value):
                """Size of the square"""
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                if value < 0:
                        raise ValueError("size must be >= 0")
                self.__size = value

        def my_print(self):
                """ prints in stdout the square with the character # """
                if self.__size > 0:
                        for i in range(self.__size):
                                print("#" * self.__size)
                else:
                        print()
