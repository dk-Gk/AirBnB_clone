#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initiallization"""

        if(len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['updated_at'] = self.updated_at.isoformat()
        d['created_at'] = self.created_at.isoformat()
        return(d)
