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
        # Remove operator from tokens list
        operator = tokens.pop(0)
        # Turn list of strings into list of integers
        # num_list = list(map(lambda x: int(x), tokens))
        num_list = [int(num) for num in tokens]

        # try:
        #     num1 = int(tokens[1])
        #     num2 = int(tokens[2])
        # except IndexError:
        #     num1 = int(tokens[1])

        if operator == "+":
            print add(num_list)

        # TO DO:
        # all of this other stuff in the bottom
        # is broken now

        elif operator == '-':
            print subtract(num_list)
        elif operator == '*':
            print multiply(num_list)
        elif operator == '/':
            print divide(num_list)
        elif operator == 'square':
            print square(num_list[0])
        elif operator == 'cube':
            print cube(num_list[0])
        elif operator == 'pow':
            print power(num_list)
        # elif operator == 'mod':
        #     print mod(num1, num2)
