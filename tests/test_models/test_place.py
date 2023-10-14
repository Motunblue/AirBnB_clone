#!/usr/bin/python3
"""
    Unittests for module models/place,py
"""
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Test instantiation of Place class"""
    c = Place()
