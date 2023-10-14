#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCityInstantiation(unittest.TestCase):
    """Test instantiation of city class"""
    def test_no_arg(self):
        """Test with no arg"""
        c = City()
