import unittest
from testowaniePython.Testowanie.rpn import RPNCalculator, OperatorMap


class RPNTests(unittest.TestCase):
    def test_add(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 1 +"
        result = calculator.calculate(expression)
        self.assertEqual(6, result)

    def test_subtract(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 1 -"
        result = calculator.calculate(expression)
        self.assertEqual(4, result)

    def test_multiply(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 2 *"
        result = calculator.calculate(expression)
        self.assertEqual(10, result)

    def test_divide(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "6 3 /"
        result = calculator.calculate(expression)
        self.assertEqual(2, result)

    def test_complex_expression(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 1 2 + 4 * + 3 -"
        result = calculator.calculate(expression)
        self.assertEqual(14, result)

    def test_invalid_operator(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 1 #"
        with self.assertRaises(ValueError):
            calculator.calculate(expression)

    def test_insufficient_operands(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 %"
        with self.assertRaises(ValueError):
            calculator.calculate(expression)


    def test_large_numbers(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "1000000 1000000 *"
        result = calculator.calculate(expression)
        self.assertEqual(1000000000000, result)

    def test_division_by_zero(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 0 /"
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(expression)

    def test_mixed_operations(self):
        operators = OperatorMap.create_operators()
        calculator = RPNCalculator(operators)
        expression = "5 2 * 3 + 10 /"
        result = calculator.calculate(expression)
        self.assertEqual(1.3, result)


if __name__ == '__main__':
    unittest.main()
