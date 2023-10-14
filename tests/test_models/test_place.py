#!/usr/bin/env python3
"""
    Unittests for module models/place,py
"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceInstantiation(unittest.TestCase):
    """Test instantiation of Place class"""
    def test_no_arg(self):
        """Test with no arg"""
        p = Place()

