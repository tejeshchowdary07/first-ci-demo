import unittest

from attrition_logic import predict_attrition_risk


class TestAttritionLogic(unittest.TestCase):

    def test_high_risk_case(self):
        result = predict_attrition_risk("Yes", 1)
        self.assertEqual(result, "HIGH")

    def test_low_risk_without_overtime(self):
        result = predict_attrition_risk("No", 1)
        self.assertEqual(result, "LOW")

    def test_low_risk_due_to_satisfaction(self):
        result = predict_attrition_risk("Yes", 4)
        self.assertEqual(result, "LOW")


if __name__ == "__main__":
    unittest.main()
