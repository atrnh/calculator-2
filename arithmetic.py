def add(num_list):
    """Returns sum of all integers in list"""
    return reduce((lambda x, y: x + y), num_list)


def subtract(num_list):
    """Return the difference of two numbers"""
    return reduce((lambda x, y: x - y), num_list)


def multiply(num_list):
    """Return the product of two numbers"""
    return reduce((lambda x, y: x * y), num_list)


def divide(num_list):
    """Return the quotient of two numbers as a float"""
    return reduce((lambda x, y: float(x) / y), num_list)


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return num ** 3


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num ** exponent


def mod(num_list):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
