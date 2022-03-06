import numpy
import re
from collections import OrderedDict
OPERANDS = OrderedDict({'^': numpy.power, '*': numpy.multiply, '/': numpy.divide, '+': numpy.add, '-': numpy.subtract})


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.split_expression()
        self.convert_numbers()

    def split_expression(self):
        """
        Using the regex split function - splits our expression to a list of numbers and operators
        """
        self.expression = re.split(r'(\D)', self.expression.replace(" ", "").replace(":", "/"))

    def convert_numbers(self):
        self.expression = [float(item) if item.isalnum() else item for item in self.expression]

    def solve(self):
        for operand, value in OPERANDS.items():
            # print(operand)
            while operand in self.expression:
                operand_position = self.expression.index(operand)
                # print(operand + '=?' + self.expression[operand_position])
                # print("to replace" + str(self.expression[operand_position - 1: operand_position + 2]))
                result = [value(self.expression[operand_position - 1], self.expression[operand_position+1])]
                self.expression[operand_position - 1: operand_position + 2] = result
                # print(self.expression)
        return self.expression


def main():
    while True:
        original_expression = input('Welcome, please enter expression to solve:\n')
        expression = Calculator(original_expression)
        print(str(expression.solve()))


if __name__ == '__main__':
    main()