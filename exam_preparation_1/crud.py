def create(matrixx, direction, value, current_position):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if not 0 <= r < 6 or not 0 <= c < 6:
        return matrixx, [r, c]
    elif matrixx[r][c] == ".":
        matrixx[r][c] = value
        return matrixx, [r, c]
    return matrixx, [r, c]


def update(matrixx, direction, value, current_position):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if not 0 <= r < 6 or not 0 <= c < 6:
        return matrixx, [r, c]
    elif not matrixx[r][c] == ".":
        matrixx[r][c] = value
        return matrixx, [r, c]
    return matrixx, [r, c]


def delete(matrixx, direction, current_position):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if not 0 <= r < 6 or not 0 <= c < 6:
        return matrixx, [r, c]
    elif not matrixx[r][c] == ".":
        matrixx[r][c] = "."
        return matrixx, [r, c]
    return matrixx, [r, c]


def read(matrixx, direction, current_position):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if not 0 <= r < 6 or not 0 <= c < 6:
        return matrixx, [r, c]
    elif not matrixx[r][c] == ".":
        print(matrixx[r][c])
        return matrixx, [r, c]
    return matrixx, [r, c]



matrix = [input().split() for x in range(6)]
input_line = input().split()
position = [int(input_line[0][1]), int(input_line[1][0])]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


while True:
    input_line = input()
    if input_line == "Stop":
        break
    input_line = input_line.split(", ")
    if input_line[0] == "Create":
        matrix, position = create(matrix, input_line[1], input_line[2], position)
    elif input_line[0] == "Update":
        matrix, position = update(matrix, input_line[1], input_line[2], position)
    elif input_line[0] == "Delete":
        matrix, position = delete(matrix, input_line[1], position)
    elif input_line[0] == "Read":
        matrix, position = read(matrix, input_line[1], position)

[print(*x) for x in matrix]