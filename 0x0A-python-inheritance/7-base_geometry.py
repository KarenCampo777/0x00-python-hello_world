#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """Raise exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
