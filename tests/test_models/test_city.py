#!/usr/bin/python3
""" Unit tests for City """
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class TestCity(unittest.TestCase):
    """ tests City """
    def test_city(self):
        """ checks City's attributes """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

if __name__ == '__main__':
    unittest.main
