lines = int(input())
cars = set()

for _ in range(lines):
    command, car = input().split(", ")
    if command == "IN":
        cars.add(car)
    else:
        cars.remove(car)

if cars:
    [print(x) for x in cars]
else:
    print('Parking Lot is Empty')
