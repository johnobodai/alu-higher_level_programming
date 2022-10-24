#!/usr/bin/python3
for j in range(90, 64, -1):
    if j % 2 == 0:
        print(f"{chr(j + 32)}", end="")
    else:
        print(f"{chr(j)}", end="")
