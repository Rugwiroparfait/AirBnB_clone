import unittest
from TestCity(unittest.TestCase):
    def test_city_initialization(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsEqual(city.state_id, "")
        self.assertIsEqual(city.name, "")

    def test_city_attributes(self):
        city = City(state_id = "123", name = "Kigali")
        self.assertIsEqual(city.state_id, "123")
        self.assertIsEqual(city.name, "Kigali")

if __name__ == "__main__":
    unittest.main()
