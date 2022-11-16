#!/usr/bin/python3
"""Defines class Mylists that inherits from list"""


class MyList(list):
    """Inheritance form superclass"""
    def __init__(self):
        """initialisation of object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
