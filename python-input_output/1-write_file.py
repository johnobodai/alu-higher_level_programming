#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text and returns num of char.
    :param filename: the name of the file to be writen into
    :type(filename) str:
    :param text: the text to be writen to the file.
    :type(text) str:
    :returns: the number of char writeen
    """
    with open(filename, mode='w', encoding='utf') as f:
        return f.write(text)


#print(write_file("asdf", "this is what i want to check for"))
