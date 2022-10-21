#!/usr/bin/python3
_alp = input()
alp = ord(_alp)
def islower(alp):
    """Checks if the given argument is lowercase"""
    if alp >= 97 and alp < 123:
        print("{} => lower".format(_alp))
    else:
        print("not lower")

islower(alp)
