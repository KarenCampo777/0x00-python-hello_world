#!/usr/bin/python3
"""Module inherit_form"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class"""
    return isinstance(obj, a_class) and not type(obj) == a_class
