#!/usr/bin/env python3
"""
    Unittests for module models/place,py
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestPlaceInstantiation(unittest.TestCase):
    """Test instantiation of Place class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        a = Place()
        self.assertIsInstance(a, Place)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_settr(self):
        a = Place()
        a.amenity_ids = [1, 2, 3]
        self.assertTrue(hasattr(a, "city_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "description"))
        self.assertTrue(hasattr(a, "number_rooms"))
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertTrue(hasattr(a, "latitude"))
        self.assertTrue(hasattr(a, "longitude"))
        self.assertTrue(hasattr(a, "amenity_ids"))
        self.assertEqual(a.amenity_ids, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
