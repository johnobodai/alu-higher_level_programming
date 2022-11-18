#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print to stdout the contents of the file."""
    with open(filename, mode 'r', encoding="utf-8") as openfile:
        print(openfile.read(), end='')
