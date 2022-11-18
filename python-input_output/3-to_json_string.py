#!/usr/bin/python3
"""Defines a function that returns JSON representation of an obj."""
import json


def to_json_string(my_obj):
    """Changes and returns JSON reps of a given stings
    :param my_obj: the string to be converted
    :type(my_obj): string
    :returns: the json representation of an object
    """
    return json.dumps(my_obj)
