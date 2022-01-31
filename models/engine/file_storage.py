#!/usr/bin/python3
'''Define class FileStorage'''
import json
import models


class FileStorage:
    '''Serializes instances to JSON file and deserializes to JSON file.'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Return the dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        k = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        d = {}
        for key, val in FileStorage.__objects.items():
            d[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(d, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.all_cls[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
