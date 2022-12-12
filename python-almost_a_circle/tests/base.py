#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model for all the classes in this porject
    
    :attr __nb_objects: The number of instantiated Bases.
    :type __nb_objects: int
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialise a new Base.

        :param id: The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else Base.__nb_objects += 1
        self.id = Base.__nb_objects

    @
