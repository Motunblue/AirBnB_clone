#!/usr/bin/env python3
"""
    Unittests for module models/city,py
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityInstantiation(unittest.TestCase):
    """Test instantiation of city class"""
    def test_no_arg(self):
        """Test instantiation without argument"""
        a = Amenity()
    
