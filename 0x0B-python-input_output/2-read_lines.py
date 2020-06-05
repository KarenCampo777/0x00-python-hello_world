#!/usr/bin/python3
"""Module"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF-8") as file:
        counter = 0
        for line in file:
            counter += 1
            if (nb_lines <= 0) or (nb_lines < counter):
                print(line, end="")
    file.close()
