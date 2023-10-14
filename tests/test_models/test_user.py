#!/usr/bin/env python3
"""
    Unittests for module models/user,py
"""
from models.user import User
from models.base_model import BaseModel
import unittest
import datetime


class TestUserInstantiation(unittest.TestCase):
    """Test instantiation of User class"""
    def test_subclass_of(self):
        """Test if instance is subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u, User)

    def test_no_arg(self):
        """Test without any argument"""
        u = User()
        self.assertIn("created_at", u.__dict__)
        self.assertIn("updated_at", u.__dict__)
        self.assertIn("id", u.__dict__)
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime.datetime)
        self.assertIsInstance(u.updated_at, datetime.datetime)

    def test_set_attr(self):
        """Test for setting attr"""
        u = User()
        u.email = "airbnb@gmail.com"
        u.password = "clone"
        u.first_name = "unittest"
        u.last_name = "Airbnb"

        self.assertTrue(hasattr("created_at", u))
        self.assertTrue(hasattr("updated_at", u))
