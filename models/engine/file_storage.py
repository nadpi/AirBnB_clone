#!/usr/bin/python3
'''task 5'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    '''class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        json_object = {}
        for key in FileStorage.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                try:
                    for key, value in json.load(f).items():
                        attri_value = eval(value["__class__"])(**value)
                        FileStorage.__objects[key] = attri_value
                except:
                    pass
