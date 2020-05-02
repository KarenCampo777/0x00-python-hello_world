#!/usr/bin/python3
def islower(c):
    for low in range(97, 122):
        if ord(c) == low:
            return True
        else:
            return False
