from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted = 0

while cups and bottles:
    cup = cups[0]
    bottle = bottles.pop()

    if bottle >= cup:
        wasted += bottle - cup
        cups.popleft()

    else:
        cups[0] -= bottle

if bottles:
    bottles = [str(x) for x in bottles]
    print(f"Bottles: {' '.join(bottles)}")
else:
    cups = [str(x) for x in cups]
    print(f"Cups: {' '.join(cups)}")

print(f"Wasted litters of water: {wasted}")


