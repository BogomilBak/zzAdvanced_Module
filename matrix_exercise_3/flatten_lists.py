from collections import deque

input_line = input().split("|")
result = deque()

for element in input_line:
    element = element.strip()
    element = [x for x in element.split()]
    result.extendleft(element[::-1])

print(' '.join(result))