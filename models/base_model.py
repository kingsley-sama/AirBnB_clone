#!/usr/bin/python3
"""This module defines the BaseModel class"""
from uuid import uuid4
import datetime
import models


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.name = kwargs.get('name', None)
            self.my_number = kwargs.get('my_number', None)
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns official string representation"""
        str_val = "[{}] ({}) {}"
        return str_val.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the public instace
        attribute updated_at with the current datetime
        """
        self.__dict__["updated_at"] = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        return (
            {
                'my_number': self.my_number,
                'name': self.name,
                '__class__': self.__class__.__name__,
                'updated_at': self.updated_at.isoformat(),
                'id': self.id,
                'created_at': self.created_at.isoformat()
            }
        )
