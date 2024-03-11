import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_initialiazation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        amenity = Amenity(name = "WIFI")
        self.assertEqual(amenity.name, "WIFI")

if __name__ == "__main__":
    unittest.main()
