from collections import deque

caffeine = [int(x) for x in input().split(", ")]
drinks = deque([int(x) for x in input().split(", ")])
status = 0

while caffeine and drinks:
    current_caffeine = caffeine.pop()
    current_drink = drinks.popleft()
    result = current_drink * current_caffeine

    if result + status <= 300:
        status += result
    else:
        drinks.append(current_drink)
        status -= 30
        if status < 0:
            status = 0

if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {status} mg caffeine.")

