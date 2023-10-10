#!/usr/bin/env python3
"""
    Contains storage class
"""

import json
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        file (str): Hold the path to JSON file for serialization and deserialization
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
        FileStorage.__objects[k] = obj.to_dict()


    def save(self):
        """serializes obj to path"""
        with open(FileStorage.__file_path, mode="a", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes obj from path"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)