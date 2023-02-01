from collections import deque

food = int(input())
queue = deque([int(x) for x in input().split()])
biggest = (max(queue))

while food > 0 and queue:
    customer = queue[0]

    if customer <= food:
        food -= customer
        queue.popleft()

    else:
        food = 0

print(biggest)
if queue:
    queue = [str(x) for x in queue]
    print(f"Orders left: {' '.join(queue)}")
else:
    print("Orders complete")
