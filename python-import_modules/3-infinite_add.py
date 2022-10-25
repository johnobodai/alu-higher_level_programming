#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    j = 0 
    k = len(argv)
    for i in range(1, k):
        j += int(argv[i])
    print(f"{j}")
