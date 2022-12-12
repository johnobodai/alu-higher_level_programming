#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model for all the classes in this porject
    :attr __nb_objects: The number of instantiated Bases.
    """

    __nb_objects = 0
