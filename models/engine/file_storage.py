#!/usr/bin/python3
"""
A Module that defines a class for File Storage
This Module is essential at this stage, in order to
get introduced to dealing with saving and loading JSON
data objects and use them along out project.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """A Class that manages JSON objects, serialization
    and deserialization.
    Methods:
        all(self): Returns the dictionary __objects
        new(self, obj): sets in __objects the obj with
        a key
        save(self): serializes __objects to JSON file
        in __file_path
        reload(self): deserializes the JSON file into
        __objects
    Class Attributes:
        __file_path: path for data storage
        __objects: dict for data to be deserialized to
        or serialized from
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns the list of objects aftere being
        serialized
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new obj into the __objects dict
        with a key className.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path
        i.e Saves the JSON representation of the
        objects into a file.
        """
        with open(self.__file_path, "w", encoding="utf8") as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the data stored in the file and saves
        it into the __objects dict
        i.e loads the data in the file and deserializes it
        for further operations on objects.
        """
        try:
            with open(self.__file_path, "r", encoding="utf8") as file:
                data = json.load(file)
                for value in data.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            pass
