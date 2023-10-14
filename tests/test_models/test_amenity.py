#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityInstantiation(unittest.TestCase):
    """Test instantiation of city class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_settr(self):
        a = Amenity()
        a.name = "pool"
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "pool")


if __name__ == "__main__":
    unittest.main()
