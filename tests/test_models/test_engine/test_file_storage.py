#!/usr/bin/python3
"""
A Module that Tests the FileStorage Class
functionalities, for storing data into a file,
saving, loading and updating this dataset.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    A Test Class for performing unittests on
    FileStorage Class and methods.
    """
    def setUp(self):
        self.test_storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.test_storage.new(obj1)
        self.test_storage.new(obj2)

    def tearDown(self):
        del self.test_storage

    def test_new(self):
        self.assertIsInstance(self.test_storage.objects, dict)
        self.assertIsNotNone(self.test_storage.objects)
        for key in self.test_storage.objects:
            self.assertIsInstance(self.test_storage.objects[key], BaseModel)

    def test_reload(self):
        test_dict = self.test_storage.objects
        self.test_storage.save()
        self.test_storage.reload()
        self.assertEqual(test_dict, self.test_storage.objects)

if __name__ == "__main__":
    unittest.main()