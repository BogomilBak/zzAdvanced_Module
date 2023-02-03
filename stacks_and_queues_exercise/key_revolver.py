from collections import deque

price_per_bullet = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(input().split())
value_intelligence = int(input())

barrel_counter = size_of_barrel
value = value_intelligence

while bullets and locks:
    current_bullet = bullets.pop()
    value -= price_per_bullet
    current_lock = int(locks[0])
    if current_bullet <= current_lock:
        print(f"Bang!")
        locks.popleft()

    else:
        print("Ping!")

    barrel_counter -= 1
    if barrel_counter == 0 and bullets:
        barrel_counter = size_of_barrel
        print("Reloading!")

    if not locks:
        break

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


