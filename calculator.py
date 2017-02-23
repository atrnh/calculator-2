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
        operator = tokens.pop(0)
        num_list = list(map(lambda x: int(x), tokens))
        # num_list = [int(num) for num in tokens]

        # try:
        #     num1 = int(tokens[1])
        #     num2 = int(tokens[2])
        # except IndexError:
        #     num1 = int(tokens[1])

        if operator == "+":
            print add(num1, num2)
            # TO DO:
            # change arguments in add() to reflect
            # changes made in arithmetic.py
            # add now takes a list of integers

        # TO DO:
        # all of this other stuff in the bottom
        # is broken now

        # elif operator == '-':
        #     print subtract(num1, num2)
        # elif operator == '*':
        #     print multiply(num1, num2)
        # elif operator == '/':
        #     print divide(num1, num2)
        # elif operator == 'square':
        #     print square(num1)
        # elif operator == 'cube':
        #     print cube(num1)
        # elif operator == 'pow':
        #     print power(num1, num2)
        # elif operator == 'mod':
        #     print mod(num1, num2)
