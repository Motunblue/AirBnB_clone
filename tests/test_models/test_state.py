#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.state import State
from models.base_model import BaseModel
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestStateInstantiation(unittest.TestCase):
    """Test instantiation of State class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        a = State()
        self.assertIsInstance(a, State)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_settr(self):
        a = State()
        self.assertTrue(hasattr(a, "name"))


if __name__ == "__main__":
    unittest.main()
