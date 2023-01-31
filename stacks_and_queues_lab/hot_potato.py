from collections import deque

input_line = input().split()

kids = deque(input_line)

counter = int(input())

while len(kids) > 1:
    for _ in range(counter - 1):
        kids.append(kids.popleft())
    print(f"Removed {kids.popleft()}")

print(f"Last is {''.join(kids)}")
