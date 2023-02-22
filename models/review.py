#!/usr/bin/python3
"""
Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity."""
        super().__init__(*args, **kwargs)
