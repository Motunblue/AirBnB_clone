#!/usr/bin/python3
"""
    Unittests for module models/user,py
"""
from models.user import User
from models.base_model import BaseModel
import unittest

class TestUserInstantiation(unittest.TestCase):
    """Test instantiation of User class"""
    def test_no_arg(self):
        """Test without any argument"""
        c = User()
