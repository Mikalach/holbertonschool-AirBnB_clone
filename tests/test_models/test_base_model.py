#!/usr/bin/python3
""" Module for BaseModel unit tests """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel"""
    def test_id(self):
        """ test of id attribute """
        self.base = BaseModel()
        self.base.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.base.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.base = BaseModel()
        self.base.created_at = datetime.now()
        self.assertIsNotNone(self.base.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.base = BaseModel()
        dic = self.base.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(BaseModel.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.base = BaseModel()
        self.base.name = "My_Model"
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.base = BaseModel()
        self.base.name = 'My_Model'
        self.base.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.base.name, read_data)

if __name__ == '__main__':
    unittest.main()
