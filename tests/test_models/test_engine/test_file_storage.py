#!/usr/bin/python3
"""unittest"""

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """class for testing filestorage class"""

    def setUp(self):
        """create instance of class"""
        self.f = FileStorage()
        b = BaseModel()

    def tearDown(self):
        """delete instance"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """check if the func returns dict"""
        d = self.f.all()
        self.assertIsInstance(d, dict)

    def test_new(self):
        """check if the method with key"""
        self.f.new(self.b)
        key = str(self.b.__class__.__name__ + "." + self.b.id)
        self.assertTrue(key in self.f._FileStorage__objects)

    def test_save(self):
        """check if __objects serialized"""
        self.f.save()
        self.f.new(self.b)
        with open("file.json") as fd:
            s = json.load(fd)
        self.assertTrue(type(s) is dict)
