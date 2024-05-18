#!/usr/bin/python3
'''task 3. BaseModel'''
import uuid
from datetime import datetime


class BaseModel:
    '''Class BaseModel'''
    def __init__(self):
        '''initialization method'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''print: [<class name>] (<self.id>) <self.__dict__>'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''updates the public instance attribute updated_at
            with the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''
        todict = self.__dict__
        todict['__class__'] = self.__class__.__name__
        todict['created_at'] = self.created_at.isoformat()
        todict['updated_at'] = self.updated_at.isoformat()
        return todict