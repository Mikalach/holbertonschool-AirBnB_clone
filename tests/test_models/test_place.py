#!/usr/bin/python3
""" Module for Place unit tests """
import unittest
from models.base_model import BaseModel
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """ test Place """
    def test_place(self):
        """ checks Place's attribute """
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main
