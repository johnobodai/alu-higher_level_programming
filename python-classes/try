#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ An instance of a Square. """

    def __init__(self, size=0, position=(0,0)):
       
       """Initialiasation of a new square
        :param size: The size of the new square.
        :type size: int
        :param position: The position of the new square.
        :type position: (int, int)
       """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the current position of the square"""
        if not isinstance(value, tuple)  
                or len(value) != 2 
                or not all(i > 0 for i in value) 
                or not all(isinstance(i,int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)


    def my_print(self):
        """Print the 2D area of the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" "*self.__position[0] + "#"*self.__size)
    

print(help(Square))
