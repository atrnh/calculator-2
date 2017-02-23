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
    elif tokens.len() == 2:
        operation = tokens[0]
        num1 = int(tokens[1])

        if operation == 'square':
            print square(num1)
        elif operation == 'cube':
            print cube(num1)

    elif tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '-':
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '*':
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '/':
        print divide(int(tokens[1]), int(tokens[2]))

    elif tokens[0] == 'pow':
        print power(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'mod':
        print mod(int(tokens[1]), int(tokens[2])) 
