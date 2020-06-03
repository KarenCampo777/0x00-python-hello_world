#!/usr/bin/python3
"""BaseGeometry module from 9-rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


"""This is the Square module"""


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
