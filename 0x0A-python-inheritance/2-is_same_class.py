#!/usr/bin/python3
""" Module "is same class".
Same class module one function, is_same_class()"""


def is_same_class(obj, a_class):
    """Verifies if an object is an instance of the specified class."""
    return type(obj) == a_class
