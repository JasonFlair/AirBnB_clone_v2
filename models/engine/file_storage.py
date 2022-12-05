#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
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

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            this_cls = {}
            for k, v in self.__objects.items():
                this_cls[k] = v
            return this_cls

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :param obj: object to be set in
        """
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        key_name = obj_class_name + "." + obj_id

        FileStorage.__objects[key_name] = obj

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

    def delete(self, obj=None):
        """
        delete obj from __objects
        """
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        key_name = obj_class_name + "." + obj_id

        del FileStorage.__objects[key_name]
