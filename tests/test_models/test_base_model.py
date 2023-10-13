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
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))

    def test_multiple_instaces(self):
        """Test equality of the ids BaseModel instances"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b3.id, b2.id)

    def test_pos_arg(self):
        """Test the instantiation positional argument"""
        b = BaseModel(2)
        b1 = BaseModel(2, 3)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "created_at"))

    def test_keyword_arg(self):
        """Test the instantiation keyword argument"""
        b = BaseModel(id=2)
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))

        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "updated_at"))

        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580", updated_at="2023-10-13T18:33:54.505580")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        
        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580", updated_at="2023-10-13T18:33:54.505580", name="Airbnb")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at")) 
        self.assertTrue(hasattr(b, "name"))
        self.assertEqual(b.name, "Airbnb")

        b = BaseModel(first_name="unittest", last_name="Airbnb")
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, "unittest")
        self.assertTrue(hasattr(b, "last_name"))
        self.assertEqual(b.last_name, "Airbnb")

        b = BaseModel(first_name=("unittest, Airbnb"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, ("unittest, Airbnb"))

        b = BaseModel(first_name=["unittest, Airbnb"])
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, ["unittest, Airbnb"])

    def test_none_arg(self):
        b = BaseModel(None)
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=None)
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_inf_arg(self):
        b= BaseModel(float('inf'))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=float('inf'))
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_nan_arg(self):
        b= BaseModel(float('nan'))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=float('nan'))
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_setattr(self):
        b = BaseModel()
        b.name = "Airbnb"
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "name"))


class TestBaseModelStrMethod(unittest.TestCase):
    """Tests the str method of BaseModel"""
    def test_no_arg(self):
        """Test with no argument"""
        b = BaseModel()
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

    def test_pos_arg(self):
        """Test str method with positional arguments"""
        b = BaseModel(2)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(None)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(float('nan'))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(float('inf'))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

    def test_keyword_arg(self):
        """Test str method with keyword instantiation"""
        b = BaseModel(name="Airbnb")
        with self.assertRaises(AttributeError):
            self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id="2")
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id=2)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id=[1, 2])
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}") 

        b = BaseModel(id=(1, 2))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")


    def test_using_str(self):
        """Test str method using __str__"""
        b = BaseModel()
        self.assertEqual(b.__str__(), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel()
        # Test __str__ with arguments
        with self.assertRaises(TypeError):
            self.assertEqual(b.__str__(23), f"[BaseModel] ({b.id}) {b.__dict__}")

class TestBaseModelSave(unittest.TestCase):
    """Test the save method of BaseModel"""
    def test_no_arg(self):
        """Test with no arg"""
        b = BaseModel()
        t1 = b.updated_at

        b.save()

        t2 = b.updated_at
        self.assertNotEqual(t1, t2)

    def test_one_arg(self):
        """Test with one arg"""
        b = BaseModel()

        with self.assertRaises(TypeError):
            b.save("2023-13-12")


if __name__ == '__main__':
    unittest.main()
