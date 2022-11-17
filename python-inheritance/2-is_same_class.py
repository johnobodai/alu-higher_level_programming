#!/usr/bin/python3
"""Checks if _is _ function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of thew specified class
    :param odj: the object to be checked
    :type a_class: the class to match the type of obj
    :return: True if is instance else False
    """

    if type(obj) == a_class:
        return True
    return False
