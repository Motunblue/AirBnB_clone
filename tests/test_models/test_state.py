#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
from models.state import State
from models.base_model import BaseModel


class TestStateInstantiation(unittest.TestCase):
    """Test instantiation of State class"""
    c = State()
