from collections import deque

input_line = input()

queue = deque()

while not input_line == "End":
    if input_line == "Paid":
        while queue:
            print(f"{queue.pop()}")
    else:
        queue.appendleft(input_line)

    input_line = input()
print(f"{len(queue)} people remaining.")
