"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    valid_operators = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
    user_input = raw_input('> ')
    tokens = user_input.split(' ') # tokenize user input

    if user_input == 'q':
        break
    else:
        operator = tokens.pop(0) # Remove operator from tokens list
        if operator in valid_operators:

            # Turn list of strings into list of integers        
            try:
                num_list = [int(num) for num in tokens]
            except ValueError:
                print 'Your input is invalid. Please enter numbers after your operator.'
                continue

            # Check operator and apply the correct operation
            if operator == "+":
                print add(num_list)
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
            elif operator == 'mod':
                print mod(num_list)
        else:
            print "Please enter a valid operator."