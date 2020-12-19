#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):

    low = 0
    high = len(list_of_integers) - 1
    while low < high:
         mid = (low + (high - low)) // 2
         if list_of_integers[mid] <= list_of_integers[mid + 1]:
            low = mid + 1
        elif list_of_integers[mid] <= list_of_integers[mid - 1]:
            high = mid - 1
        elif (list_of_integers[mid] >= list_of_integers[mid + 1] and
              list_of_integers[mid] >= list_of_integers[mid - 1]):
            return mid

    return low
