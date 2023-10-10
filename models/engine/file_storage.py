#!/usr/bin/env python3
"""
    Contains storage class
"""

import json
import os


class FileStorage:
    """Serializes and deserializes to JSON file

    Attributes:
        file (str): Hold the path to JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return dictionary object of all object
        """
        return self.__objects

    def new(self, obj):
        """Sets object"""

        k = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[k] = obj.to_dict()

    def save(self):
        """serializes obj to path"""
        with open(type(self).__file_path, mode="w", encoding="utf-8") as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        """Deserializes obj from path"""
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, encoding="utf-8") as f:
                type(self).__objects = json.load(f)
