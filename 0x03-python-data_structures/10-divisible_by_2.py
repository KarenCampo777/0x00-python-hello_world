#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    for i in my_list:
        if not i % 2:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
