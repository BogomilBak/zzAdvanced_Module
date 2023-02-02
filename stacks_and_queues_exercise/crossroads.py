from collections import deque
import re

pattern = "[A-Za-z]"
green = int(input())
yellow = int(input())
car = input()

passed = 0
crash = False
car_queue = deque()

while not car == "END":

    if not car == "green":
        car_characters = re.findall(pattern, car)
        car_queue.append(car_characters)
    else:

        while car_queue:
            current_green = green
            current_yellow = yellow

            for current_car_index in range(len(car_queue)):
                current_car = ''.join(car_queue[current_car_index])

                if current_green == 0:
                    continue

                for current_symbol in car_queue[current_car_index]:
                    if current_green > 0:
                        current_green -= 1
                        continue
                    elif current_yellow > 0:
                        current_yellow -= 1
                    else:
                        crash = True
                        print(f"A crash happened!")
                        print(f"{current_car} was hit at {current_symbol}.")
                        break

                if crash:
                    break
                passed += 1

            if crash:
                break
            car_queue.clear()

        if crash:
            break
    if crash:
        break

    car = input()

if not crash:
    print(f"Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")
