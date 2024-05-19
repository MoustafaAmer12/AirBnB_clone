#!/usr/bin/python3
"""
A Module that creates a package out of this group
of modules.
It creates an instance for file storage using the engine
"""
from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
