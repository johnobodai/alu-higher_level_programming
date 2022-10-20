#!/usr/bin/python3
alp = ord(input())
def islower(alp):
    """Checks if the given argument is lowercase"""
    if alp >= 97 and alp < 123:
        print("{} => lower".format(alp))
    else:
        print("not lower")

islower(alp)
