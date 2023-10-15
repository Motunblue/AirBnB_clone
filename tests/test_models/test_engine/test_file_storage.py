#!/usr/bin/env python3

"""Unnitests for `models/engine/file_storage.py`"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Unittest for file storage"""

    def test_instantiation(self):
        s = FileStorage()
        self.assertEqual(type(s), FileStorage)
        self.assertIsInstance(s, FileStorage)

    def test_storage_private_attr_type(self):
        s = FileStorage()
        self.assertTrue(type(s.__class__._FileStorage__objects), dict)
        self.assertTrue(type(s.__class__._FileStorage__file_path), str)

    def test_save_and_all(self):
        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()
        storage.new(a)
        storage.new(b)
        storage.new(c)
        storage.new(p)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.new(u)
        dict = storage.all()
        self.assertIn(f"Amenity.{a.id}", dict.keys())
        self.assertTrue(type(dict[f"Amenity.{a.id}"]), "Amenity")
        self.assertIn(f"BaseModel.{b.id}", dict.keys())
        self.assertTrue(type(dict[f"BaseModel.{b.id}"]), "BaseModel")
        self.assertIn(f"City.{c.id}", dict.keys())
        self.assertTrue(type(dict[f"City.{c.id}"]), "City")
        self.assertIn(f"Place.{p.id}", dict.keys())
        self.assertTrue(type(dict[f"Place.{p.id}"]), "Place")
        self.assertIn(f"Review.{r.id}", dict.keys())
        self.assertTrue(type(dict[f"Review.{r.id}"]), "Review")
        self.assertIn(f"State.{s.id}", dict.keys())
        self.assertTrue(type(dict[f"State.{s.id}"]), "State")
        self.assertIn(f"User.{u.id}", dict.keys())
        self.assertTrue(type(dict[f"User.{u.id}"]), "User")
