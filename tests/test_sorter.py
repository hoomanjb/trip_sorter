import unittest
from boarding_passes.boarding_pass import BoardingPass
from boarding_sorter.sorter import sort_boarding_passes


class TestSorter(unittest.TestCase):
    def test_sort_boarding_passes(self):
        passes = [
            BoardingPass(transport_type="Train", origin="Madrid", destination="Barcelona", seat_assignment="45B"),
            BoardingPass(transport_type="Bus", origin="Barcelona", destination="Gerona Airport"),
            BoardingPass(transport_type="Flight", origin="Gerona Airport", destination="Stockholm", gate="45B", seat_assignment="3A", extra={'baggage_drop': "344"}),
            BoardingPass(transport_type="Flight", origin="Stockholm", destination="New York JFK", gate="22", seat_assignment="7B"),
        ]
        sorted_passes = sort_boarding_passes(passes)
        expected_result = [
            passes[0],
            passes[1],
            passes[2],
            passes[3],
        ]
        self.assertEqual(sorted_passes, expected_result)


if __name__ == "__main__":
    unittest.main()
