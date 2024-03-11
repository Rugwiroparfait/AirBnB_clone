import uuid
from datetime import datetime

class Basemodel:
    """ parent class for all methods that will be needed
    """
    def __init__(self, *args, **kwargs):
        """initialize Basemodel instance."""
        if kwargs:
            for key, value in kwargs.item():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%%f")
                if key != '__class__':
                    setattr(self, key, value)
                    if 'id' not in kwargs:
                        self.id = str(uuid.uuid4())
                    if 'created_at' not in kwargs:
                        self.created_at = datetime.now()
                    if 'updated_at' not in kwargs:
                        self.updated_at = datetime.now()
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
            def __str__(self):
                """Return string representation of BaseModel."""
                return "[{}] ({})".format(self.__class__.__name__, self.id, self.__dict__)
            def save(self):
                """Update updated_at attribute with current datetime.
                """
                self.updated_at =  datetime.now()

            def to_dict(self):
                """Return  dictionary representation of Basemodel.
                """
                new_dict = self.__dict__.copy()
                new_dict['__class__'] = self.__class__.__name__
                new_dict['created_at'] = self.created_at.isoformat()
                new_dict['updated_at'] = self.updated_at_isoformat()
                return new_dict
