#!usr/bin/python3
""" Base Model Class """
import uuid
import datetime


class BaseModel:
    """ a class that defines all common
    attributes/methods for other classes """

    def __init__(self, name="", my_number=0):
        """ attributes
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime
        when an instance is created and it will be updated
        every time you change your object
        """

        self.name = name
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """  updates the public instance attribute
        updated_at with the current datetime """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """  returns a dictionary containing all keys/values
        of __dict__ of the instance """

        obj = self.__dict__.copy()
        obj.update({'__class__': type(self).__name__})
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
