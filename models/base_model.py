#!/usr/bin/python3
"""Defines the BaseModel class."""


import uuid
from datetime import datetime
import models

class BaseModel:
    """Project super class."""
    def __init__(self, *args, **kwargs):
        """Initializing base_model."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Formating the printing behavior of base_model class."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updating current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returning key and value to dict_copy."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy

