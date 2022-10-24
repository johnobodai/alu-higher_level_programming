#!/usr/bin/python3
# This function prints the last digit of a number
# @number: The number to be inputed by the user


def print_last_digit(int(number)):
    if number > 0:
        print(f"{number % 10:1d}")
    elif number < 0:
        print(f"{-(-number % 10):1d}")
    else:
        print(f"{number:1d}")
