#!/usr/bin/python3


if __name__ == "__main__":
    def _add(*kwds):
        j = 0
        for i in kwds:
            j = (j + i)
        print(f"{j}")
