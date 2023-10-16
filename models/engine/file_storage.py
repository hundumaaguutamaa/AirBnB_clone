#!/usr/bin/python3
"""Defines the files_torage class."""

import json
import os
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine."""

    file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary to __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file."""
        objdict = {}

        for key in FileStorage.__objects:
            objdict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.file_path, "w") as h:
            json.dump(objdict, h)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.isfile(self.file_path):

            with open(self.file_path, "r") as h:
                my_dict = json.load(h)

                for key, value in my_dict.items():
                    name = sys.modules[__name__]
                    my_class = getattr(name, value['__class__'])
                    self.__objects[key] = my_class(**value)
