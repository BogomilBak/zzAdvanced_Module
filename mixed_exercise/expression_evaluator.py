from collections import deque

input_line = input().split()

operations = {
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: a // b
}

result = deque()

for element in input_line:
    if element in operations:
        number = int(result.popleft())
        while result:
            number_1 = int(result.popleft())
            number = operations[element](number, number_1)
        result.append(number)
    else:
        result.append(element)

print(result.popleft())