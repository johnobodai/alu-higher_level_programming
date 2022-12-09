#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise a new Rectangle.

        :param x: The x coordinate of the new Rectangle
        :type x: int
        :param y: The y coordinate of the new Rectangle
        :type y: int
        :param id: The identity of the new Rectangle
        :type id: int
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Set the widthe of the Rectangle."""
            return self.__width
        
        @width.setter
        def width(self, value):
            self.__width = value
        
        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            return self.__x
        
        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            return self.__y
            
         @y.setter
        def y(self, value):
            self.__y = value

