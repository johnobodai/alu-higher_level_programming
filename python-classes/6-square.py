#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ An instance of a Square. """

    def __init__(self, size=0, position=(0,0)):
        """
        Initialiasation of a new square
        Parameters:
            size(int): The size of the new square.
            position(int,int): The position of the new square.
        
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple)  
                or len(value) != 2 
                or not all(i > 0 for i in value) 
                or not all(isinstance(i,int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        return (self.__size * self.__size)


    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" "*self.__position[0] + "#"*self.__size)
    

# print(help(Square))
