#!usr/bin/python3
""" module 1"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModel"""

    def __init__(self):
        """initialize a basemodel object."""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """return str """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        obj = self.__dict__.copy()
        obj.update({'__class__': type(self).__name__})
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
