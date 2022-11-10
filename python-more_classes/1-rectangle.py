#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle(self, width=0, height=0):
    """Represent a Rectangle"""
    def __init__():
        self.width = width
    
    @property
    def width(self):
        self.__width = width

    @property
    def height(self):
        self.__height = height

    @setter.width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @setter.height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
