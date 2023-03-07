size = int(input())
matrix = []
position = []
for row in range(size):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        position.append(row)
        position.append(line.index("S"))
        matrix[row][line.index("S")] = "-"
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
kills = 0
damage = 3

while True:
    command = input()
    position[0] += directions[command][0]
    position[1] += directions[command][1]
    location = matrix[position[0]][position[1]]
    if location == "*":
        damage -= 1
        matrix[position[0]][position[1]] = "-"
        if damage == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            matrix[position[0]][position[1]] = "S"
            break
    if location == "C":
        kills += 1
        matrix[position[0]][position[1]] = "-"
        if kills == 3:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[position[0]][position[1]] = "S"
            break

[print(''.join(x)) for x in matrix]