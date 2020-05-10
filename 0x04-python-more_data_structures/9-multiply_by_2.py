#!/usr/bin/python3
def multiply_by_2(a_dictionary):
# Function that returns a new dictionary multiplied by 2
# All values are only integers
    new_dictionary = a_dictionary.copy()
    for key, num in a_dictionary.items():
        new_dictionary[key] = num * 2
    return new_dictionary
