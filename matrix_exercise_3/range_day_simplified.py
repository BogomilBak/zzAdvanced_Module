def movement_action(directionz, stepz):
    r = location[0] + movement[directionz][0] * stepz
    c = location[1] + movement[directionz][1] * stepz

    if 0 > r or r > 4 or 0 > c or c > 4:
        return location
    if matrix[r][c] == "x":
        return location
    return [r, c]


def shoot_actionz(directionz):
    r = location[0] + movement[directionz][0]
    c = location[1] + movement[directionz][1]
    while 0 <= r < 5 and 0 <= c < 5:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]
        r += movement[directionz][0]
        c += movement[directionz][1]

matrix = [input().split() for x in range(5)]
count = int(input())
killed = 0
killed_location = []
total_targets = len([x for y in matrix for x in y if x == "x"])
location = []

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(5):
    for column in range(5):
        if matrix[row][column] == "A":
            location = [row, column]

for _ in range(count):
    command = input().split()

    if command[0] == "shoot":
        shoot_action = shoot_actionz(command[1])

        if shoot_action:
            killed_location.append(shoot_action)
            killed += 1

        if killed == total_targets:
            break

    elif command[0] == "move":
        direction, steps = command[1], int(command[2])
        location = movement_action(direction, steps)

if killed == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - killed} targets left.")
[print(x) for x in killed_location]