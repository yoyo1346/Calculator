def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")


def power(a, b):
    result = 1
    for _ in range(b):
        result = result * a
    return result


def modulo(a, b):
    return a % b


def factorial(a):
    result = 1
    for n in range(1, a + 1):
        result *= n
    return result


def average(a, b):
    return divide(addition(a, b), 2)


def negative(a):
    return 0 - a


