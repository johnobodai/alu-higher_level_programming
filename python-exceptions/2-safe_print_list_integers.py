#!/usr/bin/python3
# Prints the first x elements of a list and only interger


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
            count += 1
    print()
    return count
