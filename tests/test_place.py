import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_initialization(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")

    def test_place_attributes(self):
        place = Place(city_id="123", user_id = "456", name ="byangabo musanze")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Cottagee")

if __name__ == "__main__":
    unittest.main()
