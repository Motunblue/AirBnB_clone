#!/usr/bin/python3
"""
    Unittests for module models/review,py
"""
from models.review import Review
from models.base_model import BaseModel


class TestReviewInstantiation(unittest.TestCase):
    """Test instantiation of Review class"""
    c = Review()
