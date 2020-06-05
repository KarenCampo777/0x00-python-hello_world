#!/usr/bin/python3
"""Module"""


def read_file(filename=""):
    """prints stdout"""
    with open(filename, "r", encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
        my_file.close()
