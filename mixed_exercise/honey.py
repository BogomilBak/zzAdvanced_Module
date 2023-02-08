from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque(input().split())
honey = 0

opera = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if bee > nectar:
        continue
    current_operator = operators.popleft()
    if nectar > 0:
        honey += abs(opera[current_operator](bee, nectar))
    bees.popleft()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
