#!/usr/bin/python3
"""
A Module that defines an Review Class
that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A Class that defines an Review instance
    """
    place_id = ""
    user_id = ""
    text = ""