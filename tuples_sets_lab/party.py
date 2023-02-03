def is_vip(a):
    return a[0].isdigit()

lines = int(input())

guests = {input() for _ in range(lines)}

while True:
    command = input()
    if command == "END":
        break
    guests.remove(command)

print(len(guests))
vip_guests = sorted([g for g in guests if is_vip(g)])
no_vip_guests = sorted([g for g in guests if not is_vip(g)])
[print(x) for x in vip_guests]
[print(x) for x in no_vip_guests]
