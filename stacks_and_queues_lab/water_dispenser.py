from collections import deque

water_quantity = int(input())

input_line = input()
queue = deque()

while not input_line == "Start":
    queue.appendleft(input_line)
    input_line = input()

input_line = input()

while not input_line == "End":
    if input_line.startswith('refill'):
        command, water_wanted = input_line.split()
        water_quantity += int(water_wanted)
    else:
        water_wanted = int(input_line)
        if water_wanted <= water_quantity:
            print(f"{queue.pop()} got water")
            water_quantity -= water_wanted
        else:
            print(f"{queue.pop()} must wait")

    input_line = input()

print(f"{water_quantity} liters left")
