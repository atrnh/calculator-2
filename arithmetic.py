def add(num_list):
    """Returns sum of all integers in list"""
    return reduce((lambda memo, num: memo + num), num_list)


def subtract(num_list):
    """Return the difference of all integers in the list"""
    return reduce((lambda memo, num: memo - num), num_list)


def multiply(num_list):
    """Return the product of all integers in the list"""
    return reduce((lambda memo, num: memo * num), num_list)


def divide(num_list):
    """Return the quotient of all integers in the list"""
    return reduce((lambda memo, num: float(memo) / num), num_list)


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return num ** 3


def power(num_list):
    """Return num raised to the power of all integers in the list"""
    return reduce((lambda memo, exponent: memo ** exponent), num_list)


def mod(num_list):
    """Mod takes a list of numbers and return the remainder"""
    return reduce((lambda memo, num: memo % num), num_list)

def my_reduce(my_list):
    pass