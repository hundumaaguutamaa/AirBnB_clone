#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
import models
from datetime import datetime



class BaseModel:
    """BaseModel of the AirBnB project defines all common 
        attributes/methods for other classes:.
    """

    def __init__(self, *args, **kwargs):
        """Initialize an instance attributes."""

        dateformat = '%Y-%m-%dT%H:%M:%S.%f'

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        """Check if arguments passed, and assign values."""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update instance updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary of the BaseModel instance with updated value."""

        dict_data = self.__dict__.copy()
        dict_data['created_at'] = self.created_at.isoformat()
        dict_data['updated_at'] = self.updated_at.isoformat()
        dict_data['__class__'] = self.__class__.__name__
        return dict_data

    def __str__(self):
        """Print representation of the BaseModel instance."""
        clasname = self.__class__.__name__
        return "[{}] ({}) {}".format(clasname, self.id, self.__dict__)
