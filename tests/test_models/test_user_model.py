#!/usr/bin/python3

"""unittest"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """class for testing class City"""

    def setUp(self):
        """craete instance"""
        self.c = User()

    def TearDown(self):
        """delete instance"""
        del self.c

    def test_City_superclass(self):
        """checks if the class inherits from City"""
        self.assertIsInstance(self.c, BaseModel)

    def test_City_attr(self):
        """check attributes and their types"""
        self.assertTrue("email" in self.c.__dir__())
        self.assertTrue("first_name" in self.c.__dir__())
        self.assertTrue("last_name" in self.c.__dir__())
        self.assertTrue("password" in self.c.__dir__())

        self.assertIsInstance(getattr(self.c, "email"), str)
        self.assertIsInstance(getattr(self.c, "first_name"), str)
        self.assertIsInstance(getattr(self.c, "last_name"), str)
        self.assertIsInstance(getattr(self.c, "password"), str)
