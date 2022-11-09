#!/usr/bin/python3
'''Define a sqaure.'''


class Square():
    ''' Initialize a new square.'''

    def __init__(self,size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an interger')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

