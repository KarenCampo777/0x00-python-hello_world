#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle object"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for row in range(self.__height):
            string += ("#" * self.__width)
            if row != self.__height - 1:
                string += "\n"

        return string

    def __repr__(self):
        """Return repr of rectangle"""
        width = str(self.__width)
        height = str(self.__height)
        return 'Rectangle(' + width + ', ' + height + ')'
