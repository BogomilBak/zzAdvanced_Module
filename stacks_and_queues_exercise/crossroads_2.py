import sys
from collections import deque

green = int(input())
yellow = int(input())
car = input()

passed = 0
car_queue = deque()

while not car == "END":
    if not car == "green":
        car_queue.append(car)
    else:
        if car_queue:
            current = car_queue.popleft()
            time = green - len(current)
            passed += 1
            while time > 0:
                if car_queue:
                    current = car_queue.popleft()
                    time -= len(current)
                    passed += 1
                else:
                    break
            if abs(time) > yellow:
                index = yellow + time
                print(f"A crash happened!")
                print(f"{current} was hit at {current[index]}.")
                sys.exit()

    car = input()

print(f"Everyone is safe.")
print(f"{passed} total cars passed the crossroads.")
