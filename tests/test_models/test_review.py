#!/usr/bin/python3
""" Module for Review unit tests """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test Review """

    def test_review(self):
        """ checks review's attributes """
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')
        self.assertEqual(True, issubclass(Review, BaseModel))

if __name__ == '__main__':
    unittest.main