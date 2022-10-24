#!/usr/bin/python3
# This function prints numbers from 1 to 100 separated by space
# For multiples of three, five and five and three, Fizz, Buzz and FizzBuzz \
# are printed respectively


def fizzbuzz():
    for j in range(1, 101):
        if j % 3 == 0 and j % 5 == 0:
            print("FizzBuzz", end=" ")
        elif j % 3 == 0:
            print("Fizz", end=" ")
        elif j % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{j}", end=" ")
