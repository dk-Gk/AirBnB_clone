#!/usr/bin/python3

"""unittes"""

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    """test class for basemodel"""

    def setUp(self):
        """Initializing instance"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def TearDown(self):
        """Removing instance"""
        del self.base1
        del self.base2

    def test_unique_id(self):
        """Checks uniqueness of id for different onjects"""
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_id_type(self):
        """Checks that the type of the id is string"""
        self.assertEqual("<class 'str'>", str(type(self.base1.id)))

    def test_equal_val(self):
        """check if created_at and update_at are equal"""
        self.assertEqual(self.base1.created_at,
                         self.base1.updated_at)

    def test_save(self):
        """check if updated_at is updated"""
        before = self.base2.updated_at
        after = self.base2.save()
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        """check if it returns dict type and the key __class__"""
        self.assertEqual("<class 'dict'>",
                         str(type(self.base1.to_dict())))

        self.assertEqual("BaseModel", (self.base2.to_dict())["__class__"])

    def test_new_attr(self):
        """Checks for new attribute addition"""
        base2.my_number = 7
        self.assertEqual(7, base.my_number)
