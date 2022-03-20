import json


class Calculator:
    CONFIG_FILE_NAME = 'config.json'

    def __init__(self, expression):
        self.expression = expression
        self.split_expression()
        self.convert_numbers()
        configurations_dict = self.extract_configurations()
        self.parentheses = configurations_dict['parenthesis']
        self.operators = sorted(configurations_dict['operators'], key=lambda d: d['strength'])

    def split_expression(self):
        """
        Using the regex split function - splits our expression to a list of numbers and operators
        """
        self.expression = re.split(r'(\D)', self.expression.replace(" ", "").replace(":", "/"))

    def convert_numbers(self):
        self.expression = [float(item) if item.isalnum() else item for item in self.expression]

    def solve(self):
        for operator, value in self.operators:
            # print(operator)
            while operator in self.expression:
                operator_position = self.expression.index(operator)
                # print(operator + '=?' + self.expression[operator_position])
                # print("to replace" + str(self.expression[operator_position - 1: operator_position + 2]))
                result = [value(self.expression[operator_position - 1], self.expression[operator_position + 1])]
                self.expression[operator_position - 1: operator_position + 2] = result
                # print(self.expression)
        return self.expression

    def extract_configurations(self):
        with open(self.CONFIG_FILE_NAME, 'r') as config_file:
            return json.load(config_file)
