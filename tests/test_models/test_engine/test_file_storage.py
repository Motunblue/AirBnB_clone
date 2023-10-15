#!/usr/bin/env python3

"""Unnitests for `models/engine/file_storage.py`"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for file storage"""

    def test_instantiation(self):
        s = FileStorage()
        self.assertEqual(type(s), FileStorage)
        self.assertIsInstance(s, FileStorage)

    def test_storage_private_attr_type(self):
        s = FileStorage()
        self.assertTrue(type(s.__class__._FileStorage__objects), dict)
        self.assertTrue(type(s.__class__._FileStorage__file_path), str)
