#!/usr/bin/python3
def multiply_by_2(a_dictionary):
# Function that returns a new dictionary multiplied by 2
# All values are only integers
    new_dictionary = a_dictionary.copy()
    for key in a_dictionary:
        new_dictionary[key] * 2
    return new_dictionary
