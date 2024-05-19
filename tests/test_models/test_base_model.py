#!/usr/bin/python3
"""
A Module that tests the base_model class and
all its methods and attributes
"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Tests the BaseModel Class Methods and attributes
    Args:
        unittest: inherits from the unittests class
    """

    def test_class_init(self):
        """Test the correct initialization of
        class instances.
        """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertIsInstance(obj_1, BaseModel)
        self.assertIsInstance(obj_2, BaseModel)

    def test_set_attr(self):
        """Tests the correct setting of attributes
        of the instances created
        """
        obj_1 = BaseModel()
        obj_1.name = "Ahmed"
        self.assertTrue(hasattr(obj_1,"id"))
        self.assertTrue(hasattr(obj_1,"created_at"))
        self.assertTrue(hasattr(obj_1,"updated_at"))
        self.assertTrue(hasattr(obj_1,"name"))

    def test_uniq_id(self):
        """Tests that generated ids are unique
        and are not repeated
        """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        obj_3 = BaseModel()
        self.assertNotEqual(obj_1.id, obj_2.id)
        self.assertNotEqual(obj_1.id, obj_3.id)
        self.assertNotEqual(obj_2.id, obj_3.id)
    
    def test_save_updates_time(self):
        """Tests that save correctly edits the
        updated_at time
        """
        obj = BaseModel()
        update_t = obj.updated_at        
        obj.save()
        self.assertNotEqual(update_t, obj.updated_at)
    
    def test_string_represent(self):
        """Tests that the string representation
        of the object is correct
        """
        obj = BaseModel()
        self.assertNotEqual(obj, str(obj))
        self.assertEqual(str(obj),
                         f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}")
    
    def test_from_dict(self):
        """Tests the correct initialization
        of an object from dict
        """
        id = str(uuid4())
        created_at = datetime.isoformat(datetime.now())
        test_dict = {"id": id, "created_at": created_at, "name": "Ahmed", "updated_at": created_at}
        object = BaseModel(**test_dict)
        self.assertEqual(id, object.id)
        self.assertEqual(datetime.fromisoformat(created_at), object.created_at)
        self.assertEqual(datetime.fromisoformat(created_at), object.updated_at)
        self.assertEqual("Ahmed", object.name)
        self.assertIsInstance(object, BaseModel)

    def test_to_dict(self):
        """Tests the correct instantioation
        of dict from object
        """
        obj = BaseModel()
        test_dict = obj.to_dict()
        new_obj = BaseModel(**test_dict)
        self.assertIsInstance(test_dict, dict)
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertFalse(new_obj == obj)

    