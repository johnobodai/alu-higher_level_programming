#!/usr/bin/python3
"""Define a locked class"""


class LockedClass():
    """ Prevents the user from dynamically creating new instance attributes
    except if the new instance attribut is called first_name
    :param None:
    """

    __slots__ = ["first_name"]
