#!/usr/bin/python3


if __name__ == "main":
    def _add(*kwds):
        j = 0
        for i in kwds:
            j = (j + i)
        return j
