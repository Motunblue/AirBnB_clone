#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestStateInstantiation(unittest.TestCase):
    """Test instantiation of State class"""
    def test_no_arg(self):
        """Test without argument"""
        c = State()
