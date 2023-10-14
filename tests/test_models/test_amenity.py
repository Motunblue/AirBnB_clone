#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityInstantiation(unittest.TestCase):
    """Test instantiation of city class"""
    c = Amenity()
