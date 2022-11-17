#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""
    
    def __init__(self, width, height):
        """Initialisation of a new Rectangle.
        :param width: the width of the initialised rectangle
        :type int:
        :param height: the height of the initialised rectangle
        :type int
        """
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        slef.integer_validator("width", width)

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        :param name: name of the parameter
        :param value: name of parameter to validator
        :returns TypeError if value is not an interger
        :returns ValueError if value is <= 0>
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
