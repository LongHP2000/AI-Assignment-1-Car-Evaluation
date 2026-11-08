# AI Assessment 1
# Automated Testing of Rule-Based AI Algorithms
# Dataset: Car Evaluation Dataset

import csv
import unittest
from pathlib import Path

from flat_rules import classify_car as flat_ai
from hierarchical_rules import classify_car as hierarchical_ai


class TestRuleBasedAI(unittest.TestCase):

    # Test 1: Check three sample vehicles
    def test_sample_classifications(self):

        test_cases = [
            (["vhigh", "vhigh", "2", "2", "small", "low"], "unacc"),
            (["low", "low", "4", "more", "big", "high"], "vgood"),
            (["med", "med", "4", "4", "med", "med"], "acc")
        ]

        for car, expected in test_cases:

            self.assertEqual(flat_ai(car), expected)

            self.assertEqual(hierarchical_ai(car), expected)

    # Test 2: Low safety should be unacceptable
    def test_low_safety(self):

        car = ["low", "low", "4", "4", "big", "low"]

        self.assertEqual(flat_ai(car), "unacc")

        self.assertEqual(hierarchical_ai(car), "unacc")

    # Test 3: Two passenger places should be unacceptable
    def test_two_passengers(self):

        car = ["low", "low", "4", "2", "big", "high"]

        self.assertEqual(flat_ai(car), "unacc")

        self.assertEqual(hierarchical_ai(car), "unacc")

    # Test 4: Check classification outputs
    def test_valid_classifications(self):

        valid_classes = {"unacc", "acc", "good", "vgood"}

        dataset = Path(__file__).resolve().parent / "data" / "car.data"

        with dataset.open("r", encoding="utf-8") as file:

            records = list(csv.reader(file))

        self.assertEqual(len(records), 1728)

        for row in records:

            self.assertEqual(len(row), 7)

            car = row[:6]

            self.assertIn(flat_ai(car), valid_classes)

            self.assertIn(hierarchical_ai(car), valid_classes)

    # Test 5: Hierarchical AI checks incorrect input length
    def test_invalid_input_length(self):

        car = ["low", "low"]

        with self.assertRaises(ValueError):

            hierarchical_ai(car)

    # Test 6: Repeated decisions should be consistent
    def test_consistent_predictions(self):

        car = ["low", "med", "4", "4", "big", "high"]

        self.assertEqual(flat_ai(car), flat_ai(car))

        self.assertEqual(
            hierarchical_ai(car),
            hierarchical_ai(car)
        )


if __name__ == "__main__":

    unittest.main()