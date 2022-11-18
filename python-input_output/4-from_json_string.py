#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.
    :param my_str: jason string to be converted to a python string
    """
    return json.loads(my_str)
