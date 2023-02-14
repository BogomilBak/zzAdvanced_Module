presents = int(input())
rows = int(input())
matrix = [input().split() for x in range(rows)]
total_nice_kids = len([x for y in matrix for x in y if x == "V"])
given_presents = 0
santa_position = []

valid_movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "S":
            santa_position = [row, column]
            matrix[santa_position[0]][santa_position[1]] = "-"

while presents > 0 and total_nice_kids > given_presents:
    command = input()

    if command == "Christmas morning":
        break
    else:
        santa_position[0] += valid_movement[command][0]
        santa_position[1] += valid_movement[command][1]

    santa_next_position = matrix[santa_position[0]][santa_position[1]]

    if santa_next_position == "V":
        given_presents += 1
        presents -= 1
    elif santa_next_position == "C":
        for move in valid_movement:
            next_row = santa_position[0] + valid_movement[move][0]
            next_column = santa_position[1] + valid_movement[move][1]
            if presents == 0:
                break

            if matrix[next_row][next_column] == "V":
                matrix[next_row][next_column] = '-'
                given_presents += 1
                presents -= 1
            elif matrix[next_row][next_column] == "X":
                matrix[next_row][next_column] = '-'
                presents -= 1

    matrix[santa_position[0]][santa_position[1]] = "-"

remaining_kids = len([x for y in matrix for x in y if x == "V"])

if presents == 0 and total_nice_kids > given_presents:
    print("Santa ran out of presents!")
matrix[santa_position[0]][santa_position[1]] = "S"
[print(*x) for x in matrix]

if remaining_kids > 0:
    print(f"No presents for {remaining_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {given_presents} happy nice kid/s.")