#!/usr/bin/python3
# This function prints the last digit of a number
# @number: The number to be inputed by the user


def print_last_digit(number):
    if number > 0:
        print(f"{number % 10}", end="")
        return(number % 10)
    elif number < 0:
        print(f"{(-number % 10)}", end="")
        return((-number % 10))
    else:
        print(f"{number:}", end="")
        return(number)



'''
This function can also be used

def print_last_digit(number):
    print(f"{abs(number) % 10}", end="")
    return (abs(number) % 10)
'''
