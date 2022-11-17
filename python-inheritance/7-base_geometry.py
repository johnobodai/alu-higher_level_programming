#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry():
    """Represent base geometry."""

    def area(self):
        """Area of a Geo."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        :param name: name of the parameter
        :param value: name of parameter to validator
        :returns TypeError if value is not an interger
        :returns ValueError if value is <= 0>
        """
    if type(value) != int:
        raise TypeError("{} must be an interger".format(name))
    if value <= 0:
        raise ValueError("{} must be greater then 0".format(name))
