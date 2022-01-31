#!/usr/bin/python3

"""unittest"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCity(unittest.TestCase):
    """class for testing class City"""

    def setUp(self):
        """craete instance"""
        self.c = Place()

    def TearDown(self):
        """delete instance"""
        del self.c

    def test_City_superclass(self):
        """checks if the class inherits from City"""
        self.assertIsInstance(self.c, BaseModel)

    def test_City_attr(self):
        """check attributes and their types"""
        self.assertTrue("name" in self.c.__dir__())
        self.assertTrue("city_id" in self.c.__dir__())
        self.assertTrue("description" in self.c.__dir__())
        self.assertTrue("user_id" in self.c.__dir__())
        self.assertTrue("number_rooms" in self.c.__dir__())
        self.assertTrue("number_bathrooms" in self.c.__dir__())
        self.assertTrue("max_guest" in self.c.__dir__())
        self.assertTrue("price_by_night" in self.c.__dir__())
        self.assertTrue("latitude" in self.c.__dir__())
        self.assertTrue("longitude" in self.c.__dir__())
        self.assertTrue("amenity_ids" in self.c.__dir__())

        self.assertIsInstance(getattr(self.c, "name"), str)
        self.assertIsInstance(getattr(self.c, "city_id"), str)
        self.assertIsInstance(getattr(self.c, "description"), str)
        self.assertIsInstance(getattr(self.c, "user_id"), str)
        self.assertIsInstance(getattr(self.c, "number_rooms"), int)
        self.assertIsInstance(getattr(self.c, "number_bathrooms"), int)
        self.assertIsInstance(getattr(self.c, "max_guest"), int)
        self.assertIsInstance(getattr(self.c, "price_by_night"), int)
        self.assertIsInstance(getattr(self.c, "latitude"), float)
        self.assertIsInstance(getattr(self.c, "longitude"), float)
        self.assertIsInstance(getattr(self.c, "amenity_ids"), str)
