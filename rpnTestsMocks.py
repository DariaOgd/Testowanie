import unittest
from unittest.mock import MagicMock
from testowaniePython.Testowanie.rpn import RPNCalculator


class RPNTests(unittest.TestCase):
    def test_add(self):
        add_operation = MagicMock()
        add_operation.operacja.return_value = 6
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'+': add_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 1 +"
        result = calculator.calculate(expression)
        self.assertEqual(6, result)

    def test_subtract(self):
        subtract_operation = MagicMock()
        subtract_operation.operacja.return_value = 4
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'-': subtract_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 1 -"
        result = calculator.calculate(expression)
        self.assertEqual(4, result)

    def test_multiply(self):
        multiply_operation = MagicMock()
        multiply_operation.operacja.return_value = 10
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'×': multiply_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 2 ×"
        result = calculator.calculate(expression)
        self.assertEqual(10, result)

    def test_divide(self):
        divide_operation = MagicMock()
        divide_operation.operacja.return_value = 2
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'/': divide_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "6 3 /"
        result = calculator.calculate(expression)
        self.assertEqual(2, result)

    def test_complex_expression(self):
        add_operation = MagicMock()
        add_operation.operacja.side_effect = lambda x, y: x + y
        multiply_operation = MagicMock()
        multiply_operation.operacja.side_effect = lambda x, y: x * y
        subtract_operation = MagicMock()
        subtract_operation.operacja.side_effect = lambda x, y: x - y
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'+': add_operation, '-': subtract_operation, '×': multiply_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 1 2 + 4 × + 3 -"
        result = calculator.calculate(expression)
        self.assertEqual(14, result)

    def test_invalid_operator(self):
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 1 #"
        with self.assertRaises(ValueError):
            calculator.calculate(expression)

    def test_insufficient_operands(self):
        add_operation = MagicMock()
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'+': add_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 +"
        with self.assertRaises(ValueError):
            calculator.calculate(expression)

    def test_large_numbers(self):
        multiply_operation = MagicMock()
        multiply_operation.operacja.return_value = 1000000000000
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'*': multiply_operation}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "1000000 1000000 *"
        result = calculator.calculate(expression)
        self.assertEqual(1000000000000, result)

    def test_small_numbers(self):

        divide_operation = MagicMock()
        divide_operation.operacja.side_effect = lambda x, y: x / y
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'/': divide_operation}

        calculator = RPNCalculator(operator_map.create_operators())
        expression = "1 1000000000000 /"
        result = calculator.calculate(expression)
        self.assertAlmostEqual(0.000000000001, result)

    def test_invalid_expression(self):
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {'+': MagicMock()}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = "5 + 2"
        with self.assertRaises(ValueError):
            calculator.calculate(expression)


    def test_empty_expression(self):
        operator_map = MagicMock()
        operator_map.create_operators.return_value = {}
        calculator = RPNCalculator(operator_map.create_operators())
        expression = ""
        with self.assertRaises(ValueError):
            calculator.calculate(expression)


if __name__ == '__main__':
    unittest.main()
