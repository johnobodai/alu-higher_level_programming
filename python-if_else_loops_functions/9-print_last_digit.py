#!/usr/bin/python3
# This function prints the last digit of a number
# @number: The number to be inputed by the user


def print_last_digit(number):
    if number > 0:
        print("{}".format(number % 10))
    elif number < 0:
        print("{}".format(-(-number % 10)))
    else:
        print(0)
