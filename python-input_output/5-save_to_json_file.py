#!/usr/bin/python3
"""Defines a functio that writes an Obj to a text file with JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes as Odj to a text file using JSON repr"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
