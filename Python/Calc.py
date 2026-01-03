class Calculator:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def operator_function(self):
        match self.operator:
            case "+":
                return self.add()
            case "-":
                return self.subtract()
            case "*":
                return self.multiply()
            case "/":
                return self.divide()
            case _:
                return ValueError("Invalid operator")

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2