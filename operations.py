class Operacje:
    class Operacja:
        def operacja(self, num1, num2):
            pass

    class Add(Operacja):
        def operacja(self, num1, num2):
            return num1 + num2

    class Min(Operacja):
        def operacja(self, num1, num2):
            return num1 - num2

    class Mult(Operacja):
        def operacja(self, num1, num2):
            return num1 * num2

    class Div(Operacja):
        def operacja(self, num1, num2):
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2
