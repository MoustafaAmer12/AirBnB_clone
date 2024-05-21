#!/usr/bin/python3
"""
A Module that defines a City Class
that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A Class that defines a City instance
    """
    state_id = ""
    name = ""