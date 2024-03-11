import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_initializiation(self):
        def test_state_initialization(self):
            state = State()
            self.assertIsInstance(state, State)
            self.assertIsEqual(state.name, "")

        def test_state_attributes(self):
            state = State(name = "Kigali")
            self.assertEqual(start.name, "Kigali")

if __name__ == "__main__":
    unittest.main()
