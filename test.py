import unittest
import assignment as ass


class Testcode(unittest.TestCase):
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
    def test_sum(self):
        self.assertEqual(ass.main(data),[{'BMI Category': 'Very severely obese', 'Count': 1}], "Categoryshould be 'Very severely obese and count = 1")

    def test_sum_tuple(self):
        self.assertEqualass(ass.main(data),[{'BMI Category': 'Very severely obese', 'Count': 1}], "Categoryshould be 'Very severely obese and count = 1")

if __name__ == '__main__':
    unittest.main()
