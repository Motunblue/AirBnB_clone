#!/usr/bin/env python3
"""
    Contains the Base class for all other class in this Project
"""
import uuid
from datetime import datetime

class BaseModel():
    """The base class"""
    def __init__(self):
        """The instantiation method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """The class string function"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at field"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of the class instance"""
        my_dict = {}
        for k,v in self.__dict__.items():
            if (type(v) == datetime):
                v = v.isoformat()

            my_dict[k] = v

        return my_dict


