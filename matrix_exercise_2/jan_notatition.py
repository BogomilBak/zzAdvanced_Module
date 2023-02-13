import sys
from collections import deque

#input_line = [3, 4, '+']
#input_line = [5, 3, 4, '*', '-']
#input_line = [7, 33, 8, '-']
#input_line = [15, '/']
#input_line = [31, 2, '+', 11, '/']
input_line = [-1, 1, '+', 101, '*', 18, '+', 3, '/']

numbers = deque()

operation= {
    "+": lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for element in input_line:
    if element not in operation:
        numbers.append(element)
    else:
        if len(numbers) < 2:
            print(f"Error: not enough operands!")
            sys.exit()
        first = numbers.pop()
        second = numbers.pop()
        result = operation[element](second, first)
        numbers.appendleft(result)

if len(numbers) == 1:
    print(*numbers)
else:
    print("Error: too many operands!")

