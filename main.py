import Calculator


print(utils.OPERANDS)


def main():
    while True:
        original_expression = input('Welcome, please enter expression to solve:\n')
        expression = Calculator.Calculator(original_expression)
        print(str(expression.solve()))


if __name__ == '__main__':
    main()