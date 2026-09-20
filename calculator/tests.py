# calculator/tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_addition(self) -> None:
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self) -> None:
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self) -> None:
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self) -> None:
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self) -> None:
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self) -> None:
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self) -> None:
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    # Parentheses tests
    def test_simple_parentheses(self) -> None:
        result = self.calculator.evaluate("(3 + 5)")
        self.assertEqual(result, 8)

    def test_parentheses_with_precedence(self) -> None:
        result = self.calculator.evaluate("(10 - 4) * 3")
        self.assertEqual(result, 18)

    def test_nested_parentheses(self) -> None:
        result = self.calculator.evaluate("((2 + 3) * 4)")
        self.assertEqual(result, 20)

    def test_multiple_parentheses(self) -> None:
        result = self.calculator.evaluate("(2 * 3) + (8 / 2) - (5 - 1)")
        self.assertEqual(result, 6)

    def test_unmatched_closing_parenthesis(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 + 5)")

    def test_unmatched_opening_parenthesis(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("(3 + 5")

    def test_parentheses_with_spaces(self) -> None:
        result = self.calculator.evaluate("( 3 + 5 )")
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()