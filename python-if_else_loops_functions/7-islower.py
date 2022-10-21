#!/usr/bin/python3
alq = input()
alp = ord(alq)
def islower(alp):
    """Checks if the given argument is lowercase"""
    if alp >= 97 and alp < 123:
        print("{} => lower".format(alq))
    else:
        print("not lower")

islower(alp)
