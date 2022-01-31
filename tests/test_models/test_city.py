#!/usr/bin/python3

"""unittest"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """class for testing class City"""

    def setUp(self):
        """craete instance"""
        self.c = City()

    def TearDown(self):
        """delete instance"""
        del self.c

    def test_City_superclass(self):
        """checks if the class inherits from City"""
        self.assertIsInstance(self.c, BaseModel)

    def test_City_attr(self):
        """check attributes and their types"""
        self.assertTrue("name" in self.c.__dir__())
        self.assertTrue("state_id" in self.c.__dir__())
        self.assertIsInstance(getattr(self.c, "name"), str)
        self.assertIsInstance(getattr(self.c, "state_id"), str)
