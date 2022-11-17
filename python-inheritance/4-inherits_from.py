#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks for inheritance.
    :param obj: the object to check
    :type a_class: the class to check if the inherita form
    :returns: True if the object is an insatance of a class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
