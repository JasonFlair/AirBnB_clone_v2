#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dict = {}
        for k, v in FileStorage.__objects.items():
            obj_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as FILE:
            json.dump(obj_dict, FILE)

    def reload(self):
        """
        deserializes the JSON file to __objects
        does nothing if file is not found
        """
        try:
            with open(FileStorage.__file_path, "r") as read_file:
                dummy_dict = json.load(read_file)
                for k, v in dummy_dict.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass

