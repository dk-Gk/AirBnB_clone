#!/usr/bin/python3

"""unittest"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestCity(unittest.TestCase):
    """class for testing class City"""

    def setUp(self):
        """craete instance"""
        self.c = Review()

    def TearDown(self):
        """delete instance"""
        del self.c

    def test_City_superclass(self):
        """checks if the class inherits from City"""
        self.assertIsInstance(self.c, BaseModel)

    def test_City_attr(self):
        """check attributes and their types"""
        self.assertTrue("place_id" in self.c.__dir__())
        self.assertTrue("user_id" in self.c.__dir__())
        self.assertTrue("text" in self.c.__dir__())

        self.assertIsInstance(getattr(self.c, "place_id"), str)
        self.assertIsInstance(getattr(self.c, "user_id"), str)
        self.assertIsInstance(getattr(self.c, "text"), str)
