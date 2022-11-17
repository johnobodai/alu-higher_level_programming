#!/usr/bin/python3
"""Defines a function to check for instance"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of or inherited instance of a class
    :param obj: the object to be checked
    :type a_class: the class to be compared to
    :returns: True if is an instace of a_class or it's inheritance
              else False
    """
    if isinstance(obj, a_class):
        return True
    return False
