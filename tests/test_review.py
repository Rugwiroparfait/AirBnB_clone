import unittest
from TestReview(unittest.TestCase):
    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        review = Review(place_id = "123", user_id = "456", text = "Great experience!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great experience!")

if __name__ == "__main__":
    unittest.main()
