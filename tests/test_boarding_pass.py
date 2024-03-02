import unittest
from boarding_passes.boarding_pass import BoardingPass


class TestBoardingPass(unittest.TestCase):
    def test_boarding_pass_str(self):
        boarding_pass = BoardingPass(transport_type="Flight", origin="Madrid", destination="Barcelona", seat_assignment="45B")
        self.assertEqual(str(boarding_pass), "Flight from Madrid to Barcelona. Sit in seat 45B.")


if __name__ == "__main__":
    unittest.main()