#!usr/bin/python3
""" module 1"""
""" the imports """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ class BaseModel defines all common
        attributes/methods for other classes
        Public instance attributes:
        - id: string - assigned with a uuid when an instance is created.
        - created_at: datetime - assigned with the current datetime
        when an instance is created.
        - updated_at: datetime - assigned with the current datetime
        when an instance is created and updated on object changes.
        """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """  updates the public instance attribute
        updated_at with the current datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """  returns a dictionary containing all keys/values
        of __dict__ of the instance """

        obj = self.__dict__.copy()
        obj.update({'__class__': type(self).__name__})
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
