#!/usr/bin/python3
"""Defines a function that append a string at the end of a text."""


def append_write(filename="", text=""):
    """Appends a string to the end of a file.
    :param filename: the file to append to
    :param text: the text to be appended to the file
    :type(filename): int
    :type(text): int
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
