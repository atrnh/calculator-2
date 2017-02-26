"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


print "Instructions: type 'q' to quit and 'd' to change how many decimal " \
      "places you want to see"

precision = 2
valid_operators = [
    '+',
    '-',
    '*',
    '/',
    '%'
]

while True:
    user_input = raw_input('> ')
    tokens = user_input.split(' ') # tokenize user input

    stack = []

    if user_input == 'q':
        break
    elif user_input == 'd':
        print 'How many decimal places do you want to see?'
        precision = int(raw_input('> '))
        print 'Your precision is now %i' % precision
        continue
    else:
        while len(tokens) > 0:
            token = tokens.pop()
            if token not in valid_operators:
                stack.append(token)
            elif token in valid_operators:
                try:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                except:
                    print "Illegal number of operands. Try again."

                if token is '+':
                    stack.append(add([num1, num2]))
                elif token is '-':
                    stack.append(subtract([num1, num2]))
                elif token is '*':
                    stack.append(multiply([num1, num2]))
                elif token is '/':
                    stack.append(divide([num1, num2]))
                elif token is '%':
                    stack.append(mod([num1, num2]))
        print stack[0]
