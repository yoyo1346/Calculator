import numpy
import re
from collections import OrderedDict
# coding=utf-8
# This is a sample Python script.
OPERANDS = OrderedDict({'*': numpy.multiply, '/': numpy.divide, '+': numpy.add, '-': numpy.subtract})


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
        print(self.expression)

    def convert_numbers(self):
        self.expression = [float(item) if item.isalnum() else item for item in self.expression]
        print(self.expression)

    def solve(self):
        for operand, value in OPERANDS.items():
            print(operand)
            # if operand in self.expression:
            #     operand_position = self.expression.index(operand)
            #     print(str(value(5, 6)))
            #     print(operand)
            #     self.expression[operand_position - 1] = value(self.expression.pop(operand_position - 1), self.expression.pop(operand_position))
            #     print self.expression

        return self.expression


def main():
    original_expression = raw_input('Welcome, please enter expression to solve:\n')
    expression = Calculator(original_expression)
    expression.solve()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
