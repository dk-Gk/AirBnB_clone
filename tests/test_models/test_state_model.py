#!/usr/bin/python3

"""unittest"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """class for testing class Amenity"""

    def setUp(self):
        """craete instance"""
        self.a = State()

    def TearDown(self):
        """delete instance"""
        del self.a

    def test_State_superclass(self)
        """checks if the class inherits from City"""
        self.assertIsInstance(self.a, BaseModel)

    def test_State_attr(self):
        """check attributes and their types"""
        self.assertTrue("name" in self.a.__dir__())
        self.assertIsInstance(getattr(self.a, "name"), str)
