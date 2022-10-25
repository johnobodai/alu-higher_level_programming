#!/usr/bin/python3

def _add(*kwds):
    j = 0
    for i in kwds:
        j = (j + i)
    return j
