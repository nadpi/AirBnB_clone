#!/usr/bin/python3
'''task 5'''
import json
import os
from models.base_model import BaseModel


class FileStorage:
    '''class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        FileStorage.__objects[str(obj.__class__.__name__) + '.' + str(obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        json_object = {}
        for key in FileStorage.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = attri_value
