from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(list(input()))

for r in range(rows):
    result = deque()
    for c in range(columns):
        element = snake.popleft()
        snake.append(element)
        if r % 2 == 0:
            result.append(element)
        else:
            result.appendleft(element)

    print(''.join(result))