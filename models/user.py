#!/usr/bin/python3
"""
A Module that defines a User Class
with user-specific attributes and some
methods that can work for users
"""
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class that defines user instances,
    with the prescribed methods allowed for users
    to perform in the cmd.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
