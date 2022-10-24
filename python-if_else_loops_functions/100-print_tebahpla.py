#!/usr/bin/python3
for j in range(90, 64, -1):
        print(f"{chr(j + 32)}" if j % 2 == 0 else f"{chr(j)}", end="")
