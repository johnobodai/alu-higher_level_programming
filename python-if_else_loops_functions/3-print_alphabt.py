#!/usr/bin/python3
# This code prints lowercase alpha but e and q
# @i - interger value that represents the ascii dec digit

for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    else:
        print("{}".format(chr(i)), end='')
