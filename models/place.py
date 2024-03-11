from models.base_model import Basemodel

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city.id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.numberbathrooms = 0
        self.max_guest = 0
        self.price_by_nights = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
