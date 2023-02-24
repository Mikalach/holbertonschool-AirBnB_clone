#!/usr/bin/python3
""" Module for State's unit tests """
import unittest
from models.base_model import BaseModel
from models.state import State
import os


class TestState(unittest.TestCase):
    """ test State """

    def test_state(self):
        """ checks State's attribute """
        self.assertEqual(State.name, '')

if __name__ == '__main__':
    unittest.main
