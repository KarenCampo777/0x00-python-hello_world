#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nlist = my_list.copy()
    if idx < 0 and idx > len(nlist):
        return nlist
    nlist[idx] = element
    return nlist
