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
    elif tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '-':
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '*':
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == '/':
        print divide(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'square':
        print square(int(tokens[1]))
