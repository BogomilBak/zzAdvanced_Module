def movement_action(directions):
    r = location[0] + movement[directions][0]
    c = location[1] + movement[directions][1]

    if 0 > r or r >= rows or 0 > c or c >= rows:
        return []
    return [r, c]


rows = int(input())
matrix = [input().split() for x in range(rows)]
location = []
movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "A":
            location = [row, column]
            matrix[row][column] = "*"

collected = 0
while collected < 10:
    command = input()
    location = movement_action(command)
    if not location:
        print(f"Alice didn't make it to the tea party.")
        break
    elif matrix[location[0]][location[1]] == "R":
        matrix[location[0]][location[1]] = "*"
        print(f"Alice didn't make it to the tea party.")
        break
    elif matrix[location[0]][location[1]].isdigit():
        collected += int(matrix[location[0]][location[1]])

    matrix[location[0]][location[1]] = "*"

if collected > 9:
    print(f"She did it! She went to the party.")
[print(*x) for x in matrix]

