from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])
created = 0

while created < 5 and chocolates and milk:
    current_chocolate = chocolates[-1]
    current_milk = milk[0]

    if current_milk <= 0 and current_chocolate <= 0:
        chocolates.pop()
        milk.popleft()
        continue
    elif current_chocolate <= 0:
        chocolates.pop()
        continue
    elif current_milk <= 0:
        milk.popleft()
        continue
    elif current_chocolate == current_milk:
        chocolates.pop()
        milk.popleft()
        created += 1
    elif not current_milk == current_chocolate:
        milk.append(milk.popleft())
        chocolates[-1] -= 5

if created == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")

