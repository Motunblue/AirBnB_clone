#!/usr/bin/env python3
"""
    Test suite for class 'BaseModel' of module `models/base_model'
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelInstantiation(unittest.TestCase):
    """Test BaseModel instantiation"""
    def test_no_arg(self):
        b = BaseModel()
        self.assertTrue(b.id)
        today = datetime.datetime.now()
        self.assertEqual(
                b.created_at.strftime("%y-%m-%d-%h"), today.strftime("%y-%m-%d-%h"))
        self.assertEqual(
                b.updated_at.strftime("%y-%m-%d-%h"), today.strftime("%y-%m-%d-%h"))

    def test_multiple_instaces(self):
        """Test equality of the ids BaseModel instances"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b3.id, b2.id)


if __name__ == '__main__':
    unittest.main()
