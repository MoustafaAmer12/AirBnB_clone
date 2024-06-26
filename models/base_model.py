#!/usr/bin/python3
"""BaseModel Module defines a blue print for all other classes
to be used in this project.
BaseModel Class is defined that standardizes an interface
for dealing with other subclasses throughout the AirBnB Project.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """A Class that acts as an interface and a blueprint for
    all other classes to inherit from it their implementation
    Methods:
        __init__(self, *args, **kwargs): Constructor for the
        class.
        save(self): Updates the file
        to_dict(self): Sets up the JSON serialization of the
        objects.
        __str__(self): Returns a string representation of the
        class
    """
    def __init__(self, *args, **kwargs):
        """A constructor for the class
        Attributes:
            *args: a tuple containing arguments, not used
            **kwargs: a list of key, value pair of args
        """
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid4())
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                self.__dict__[f"{key}"] = value

    def __str__(self):
        """A method that extracts a string representation
        of the object
        Returns:
            String representation of an object that
            can be used for further storage.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        Updates the object for now and edits its
        last updated time.
        Side effect is only updating the updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts a BaseModel or a descnedant object
        into a dictionary
        This is basically used as a base for the JSON
        serialization.
        """
        my_dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                value = value.isoformat()
            my_dict[key] = value
        return my_dict
