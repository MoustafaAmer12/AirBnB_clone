#!/usr/bin/python3
"""
A Module that defines an Amenity Class
that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A Class that defines an Amenity instance
    """
    name = ""