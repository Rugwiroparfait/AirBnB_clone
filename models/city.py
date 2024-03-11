from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwarfs)
        self.state_id = ""
        self.name = ""
