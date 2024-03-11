from models.base_model import baseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.name = ""
