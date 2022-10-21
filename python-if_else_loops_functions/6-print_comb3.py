#!/usr/bin/python3
result = ""
for i in range(8):
    for j in range(10):
        if j != i and j > i:
            print("{}{}".format(i, j), end=', ')
print("89")
