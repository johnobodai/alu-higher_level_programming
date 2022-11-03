#!/usr/bin/python3
# Prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
