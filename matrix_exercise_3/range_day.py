matrix = [input().split() for x in range(5)]
count = int(input())
killed = 0
killed_location = []
total_targets = len([x for y in matrix for x in y if x == "x"])
location = []

for row in range(5):
    for column in range(5):
        if matrix[row][column] == "A":
            location = [row, column]

for _ in range(count):

    if killed == total_targets:
        break

    command = input().split()

    if command[0] == "shoot":
        direction = command[1]
        movement = 0
        if direction == "up":
            while location[0] + movement >= 0:
                if matrix[location[0] + movement][location[1]] == "x":
                    killed += 1
                    matrix[location[0] + movement][location[1]] = "."
                    killed_location.append([location[0] + movement, location[1]])
                    break
                else:
                    movement -= 1
        elif direction == "down":
            while location[0] + movement < 5:
                if matrix[location[0] + movement][location[1]] == "x":
                    killed += 1
                    matrix[location[0] + movement][location[1]] = "."
                    killed_location.append([location[0] + movement, location[1]])
                    break
                else:
                    movement += 1
        elif direction == "left":
            while location[1] + movement >= 0:
                if matrix[location[0]][location[1] + movement] == "x":
                    killed += 1
                    matrix[location[0]][location[1] + movement] = "."
                    killed_location.append([location[0], location[1] + movement])
                    break
                else:
                    movement -= 1
        elif direction == "right":
            while location[1] + movement < 5:
                if matrix[location[0]][location[1] + movement] == "x":
                    killed += 1
                    matrix[location[0]][location[1] + movement] = "."
                    killed_location.append([location[0], location[1] + movement])
                    break
                else:
                    movement += 1

    elif command[0] == "move":
        direction, steps = command[1], int(command[2])
        max_movement = steps
        if direction == "up":
            if location[0] - steps < 0:
                max_movement = location[0]
            while max_movement > 0:
                if not matrix[location[0] - max_movement][location[1]] == ".":
                    max_movement -= 1
                else:
                    location[0] -= max_movement
                    break
        elif direction == "down":
            if location[0] + steps > 4:
                max_movement = 4 - location[0]
            while max_movement > 0:
                if not matrix[location[0] + max_movement][location[1]] == ".":
                    max_movement -= 1
                else:
                    location[0] += max_movement
                    break
        elif direction == "left":
            if location[1] - steps < 0:
                max_movement = location[1]
            while max_movement > 0:
                if not matrix[location[0]][location[1] - max_movement] == ".":
                    max_movement -= 1
                else:
                    location[1] -= max_movement
                    break
        elif direction == "right":
            if location[1] + steps > 4:
                max_movement = 4 - location[1]
            while max_movement > 0:
                if not matrix[location[0]][location[1] + max_movement] == ".":
                    max_movement -= 1
                else:
                    location[1] += max_movement
                    break

if killed == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - killed} targets left.")
[print(x) for x in killed_location]