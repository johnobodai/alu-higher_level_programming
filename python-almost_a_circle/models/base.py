#!/usr/bin/python3
"""This modules defines a Base class function"""


class Base:
    """This class is the base class of these module"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base
        :param id: The idintity of the new Base
        :type id: int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
