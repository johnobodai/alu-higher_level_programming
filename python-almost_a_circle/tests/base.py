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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json of a list of dicts

        :param list_dictionaries:A list dic
        :type list_dictionaries: list of list
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json of a list to obj to a file.
       
       :param list_objs: A list of inherited base instance
       :type list_objs: list of list
       """
       filename = cls.__name__ + ".json"
       with open(filename, "w") as jsonfile:
           if list_objs is None:
               jsonfile.write("[]")
           else:
               list_dicts = [o.to_dictionary() for o in list_objs]
               jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the of a json string

        :param json_string: a json str reps of a list of dicts
        :type json_string: string
        :returns:an empty list if str is none or empty
                    else the python list representation by json_string
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    
    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of Json strings.
        Reads form `,cls.__name__..json`.
        :returns: if the file does not exist then an empty list
                  else a list of instantiated classes#
        """
    filename = str(cls.__name__) + ".json"
    try:
        with open(filename, "r") as jsonfile:
            list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
