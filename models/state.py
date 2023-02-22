#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City."""
        super().__init__(*args, **kwargs)
