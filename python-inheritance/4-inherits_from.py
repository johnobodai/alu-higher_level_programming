#!/usr/bin/python3
"""A function that that checks for inheritance"""


def inherits_form(obj, a_class):
    """Checks for inheritance
    :param obj: the object to check
    :type a_class: the class to check if the inherita form
    :returns: True if the object is an insatance of a class
              else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
