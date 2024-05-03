from testowaniePython.Testowanie.operations import Operacje


class OperandChecker:
    @staticmethod
    def is_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False


class OperatorMap:
    @staticmethod
    def create_operators():
        operators = {}
        operators['+'] = Operacje.Add()
        operators['-'] = Operacje.Min()
        operators['*'] = Operacje.Mult()
        operators['/'] = Operacje.Div()
        return operators


class RPNCalculator:
    def __init__(self, operators):
        self.operators = operators

    def calculate(self, expression):
        elements = expression.split()
        stack = []

        for element in elements:
            if OperandChecker.is_number(element):
                stack.append(int(element))
            else:
                operator = element[0]
                operacja = self.operators.get(operator)

                if operacja is not None:
                    if len(stack) < 2:
                        raise ValueError("Not enough numbers: " + element)

                    num2 = stack.pop()
                    num1 = stack.pop()
                    result = operacja.operacja(num1, num2)
                    stack.append(result)
                else:
                    raise ValueError("Unknown operator: " + element)

        if not stack:
            raise ValueError("No result. Check the expression validity.")

        if len(stack) > 1:
            raise ValueError("Invalid number of operators. Check the expression validity.")

        return stack.pop()


# Example usage:
if __name__ == "__main__":
    operators = OperatorMap.create_operators()
    calculator = RPNCalculator(operators)
    result = calculator.calculate("3 4 + 5 6 + ×")
    print("Result:", result)
