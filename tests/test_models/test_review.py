#!/usr/bin/python3
"""
    Unittests for module models/review,py
"""
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewInstantiation(unittest.TestCase):
    """Test instantiation of Review class"""
    def test_no_arg(self):
        c = Review
