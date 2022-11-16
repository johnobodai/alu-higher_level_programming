#!/usr/bin/python3
def magic_string():
    magic_string.num_of_times = getattr(magic_string, 'num_of_times', 0) + 1
    return "BestSchool, " * (magic_string.num_of_times) + "BestSchool"
