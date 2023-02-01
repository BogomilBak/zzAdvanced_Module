from collections import deque

rounds = int(input())

queue = deque()

for _ in range(rounds):
    input_line = [int(x) for x in input().split()]
    queue.append(input_line)

for attempt in range(len(queue)):
    flag = True
    current_petrol = 0
    for petrol, distance in queue:
        current_petrol += petrol
        if distance > current_petrol:
            flag = False
            break
        current_petrol -= distance
    if flag:
        print(attempt)
        break
    else:
        queue.append(queue.popleft())
