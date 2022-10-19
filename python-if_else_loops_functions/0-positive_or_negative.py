#!/usr/bin/python3
import random


number = random.randint(-10, 10)
def pnive(arg):
    if arg > 0:
        print(f"{arg} is positive")
    elif arg < 0:
        print(f"{arg} is negative")
    else:
        print(f"{arg} is zero")

pnive(number)
