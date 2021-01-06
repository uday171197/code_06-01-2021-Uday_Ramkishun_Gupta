import unittest
import assignment as ass


class Testcode(unittest.TestCase):

    def test_sum(self):
        try:
            data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
            self.assertEqual(ass.main(data),[{'BMI Category': 'Very severely obese', 'Count': 1}], "Categoryshould be 'Very severely obese and count = 1")
            print('This function pass the test case')

        except Exception as ex:
            print(ex)
            print('This function did not pass the test case')

    def test_sum_tuple(self):
        try:
            data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
            self.assertEqual(ass.main(data),[{'BMI Category': ' severely obese', 'Count': 1}], "Categoryshould be 'Very severely obese and count = 1")
        except Exception as ex:
            print(ex)
            print('This function did not pass the test case')

if __name__ == '__main__':
    unittest.main()
