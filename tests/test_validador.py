import unittest
from scripts.validador_fifa import validate_positions

class TestValidadorFIFA(unittest.TestCase):

    def test_validate_positions_valid(self):
        self.assertTrue(validate_positions("ST|CF"))
        self.assertTrue(validate_positions("GK"))

    def test_validate_positions_invalid(self):
        self.assertFalse(validate_positions("INVALID"))
        self.assertFalse(validate_positions("ST|INVALID"))

if __name__ == "__main__":
    unittest.main()
