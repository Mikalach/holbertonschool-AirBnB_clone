#!/usr/bin/python3
""" Modules for Amenity unit tests"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests Amenity """
    def test_city(self):
        """ checks Amenity's attributes """
        self.assertEqual(Amenity.name, "")


if __name__ == '__main__':
    unittest.main
