#!/usr/bin/python3

"""Module"""

from models.base import Base


class Rectangle(Base):
    """It is a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y