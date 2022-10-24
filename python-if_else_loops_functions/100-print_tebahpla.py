#!/usr/bin/python3
for j in range(90, 64, -1):
    print("{}".format(chr(j + 32) if j % 3 == 0 else "{}".format(chr(j))), end="")
