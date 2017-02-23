"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = raw_input('> ')
    tokens = user_input.split(' ')

    if user_input == 'q':
        break
    else:
        operator = tokens[0]
        try:
            num1 = int(tokens[1])
            num2 = int(tokens[2])
        except:
            num1 = int(tokens[1])

        if operator == "+":
            print add(num1, num2)
        elif operator == '-':
            print subtract(num1, num2)
        elif operator == '*':
            print multiply(num1, num2)
        elif operator == '/':
            print divide(num1, num2)
        elif operator == 'square':
            print square(num1)
        elif operator == 'cube':
            print cube(num1)
        elif operator == 'pow':
            print power(num1, num2)
        elif operator == 'mod':
            print mod(num1, num2)
