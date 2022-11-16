#!/usr/bin/python3
"""Defines a lookup funtion"""


def lookup(obj):
    """Return a list of an available attributes and method of an object"""
    return (dir(obj))
