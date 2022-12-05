#!/usr/bin/python3
"""Integers addition: This modules works on the addition of integers"""


def add_integers(a, d=98):
    """This function adds two integers

    :param a:The first integer
    :type a: int
    :param b: The second integer whose default value is 98
    :type b: int
    :returns: The addition of a and b
    :rtype: int
    :Raises: TypeError if either a or b is not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(a, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
