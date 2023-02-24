#!/usr/bin/python3
""" Unittest for User """
import unittest
from models.base_model import BaseModel
from models.user import User
import os

#!/usr/bin/python3
"""Test cases for User Class"""

class TestUser(unittest.TestCase):
    """ test User """

    def test_user(self):
        """ checks user's attributes """
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.email))


if __name__ == '__main__':
    unittest.main
