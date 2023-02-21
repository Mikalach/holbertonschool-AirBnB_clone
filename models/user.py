#!/usr/bin/python3
"""
User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")

    def to_dict(self):
        """Return a dictionary representation of User"""
        dict_copy = super().to_dict()
        dict_copy["email"] = self.email
        dict_copy["password"] = self.password
        dict_copy["first_name"] = self.first_name
        dict_copy["last_name"] = self.last_name
        return dict_copy
