#!/usr/bin/env python3
"""
    Test suite for class 'BaseModel' of module `models/base_model'
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelInstantiation(unittest.TestCase):
    """Test BaseModel instantiation"""
    def test_no_arg(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))

    def test_multiple_instaces(self):
        """Test equality of the ids BaseModel instances"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b3.id, b2.id)

    def test_pos_arg(self):
        """Test the instantiation positional argument"""
        b = BaseModel(2)
        b1 = BaseModel(2, 3)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "created_at"))

    def test_keyword_arg(self):
        """Test the instantiation keyword argument"""
        b = BaseModel(id=2)
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))

        b = BaseModel(id=2, created_at=2023-10-13)
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "updated_at"))

        b = BaseModel(id=2, created_at="2023, 10, 13, 18, 33, 54, 505580", updated_at="2023, 10, 13, 18, 33, 54, 505580")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        
        b = BaseModel(id=2, created_at="2023, 10, 13, 18, 33, 54, 505580", updated_at="2023, 10, 13, 18, 33, 54, 505580", name="Airbnb")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at")) 
        self.assertTrue(hasattr(b, "name"))
        self.assertEqual(b.name, "Airbnb")

        b = BaseModel(first_name="unittest", last_name="Airbnb")
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, "unittest")
        self.assertTrue(hasattr(b, "last_name"))
        self.assertEqual(b.last_name, "Airbnb")

if __name__ == '__main__':
    unittest.main()
